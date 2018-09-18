import requests
import webbrowser

class FWMissionNavigator():
    
    client_id = 'cdf05b93645545e0a844c4a0d80fbef0'
    clientToken = 'Y2RmMDViOTM2NDU1NDVlMGE4NDRjNGEwZDgwZmJlZjA6RGNMSkhZazdxMkdyOGx1Y25wbmdtN0FSWTVwaEt2SlVTYjVHb2p5eg=='
    scopes = ('esi-ui.write_waypoint.v1+')
    
    def Authorize(self):
        sso_url = 'https://login.eveonline.com/oauth/authorize/?response_type=code'
        sso_url += '&client_id=' + self.client_id
        sso_url += '&redirect_uri=http://127.0.0.1:8000'
        sso_url += '&scope=' + self.scopes
        
        webbrowser.open(sso_url[0:-1])
        auth_code = input('Please login via SSO and paste the Auth code URL here:\n').split('http://127.0.0.1:8000/?code=')[1]
        
        authorization = 'Basic ' + self.clientToken
        r = requests.post('https://login.eveonline.com/oauth/token', headers={'Authorization':authorization},
                          data={'grant_type':'authorization_code', 'code':auth_code})
        token = r.json()
        if 'error' in token:
            raise BaseException('Something bad happened!')
        self.token = token
        self.session = requests.Session()
        self.session.headers.update({'Authorization':'Bearer ' + self.token['access_token']})
    
    def SetWaypoint(self, destination_id):
        wp_url = 'https://esi.tech.ccp.is/latest/ui/autopilot/waypoint/?add_to_beginning=false&clear_other_waypoints=false&datasource=tranquility&destination_id=%s' % destination_id
        self.session.post(wp_url)
    
    def SetWaypoints(self):
        galmilsystems = [system['solar_system_id'] for system in
                         self.session.get('https://esi.tech.ccp.is/latest/fw/systems/?datasource=tranquility').json()
                         if system['occupier_faction_id'] == 500004]
        
        systemlookup = {60010333: 30003836,
                         60015080: 30004980,
                         60015081: 30004998,
                         60015082: 30005298,
                         60015083: 30005297,
                         60015084: 30003842,
                         60015085: 30003825,
                         60015086: 30003828,
                         60015087: 30003853,
                         60015088: 30003788,
                         60015089: 30003792,
                         60015090: 30003795,
                         60015091: 30003799,
                         60015092: 30005308,
                         60015142: 30004973,
                         60015143: 30005307,
                         60015144: 30004993,
                         60015145: 30003830}
        
        route = [60015084, # Esesier IX - Federal Defense Union Logistic Support
                60015087, # Mercomesier III - Federal Defense Union Logistic Support
                60015145, # Orvolle VII - Federal Defense Union Logistic Support
                60015142, # Caslemon III - Federal Defense Union Logistic Support
                60015144, # Villore VI - Federal Defense Union Logistic Support
                60015081, # Parts I - Federal Defense Union Logistic Support
                60015080, # Fliet III - Federal Defense Union Logistic Support
                60015082, # Costolle V - Federal Defense Union Logistic Support
                60015092, # Jufvitte IV - Federal Defense Union Logistic Support
                60015083, # Ouelletta II - Federal Defense Union Logistic Support
                60015091, # Uphallant II - Federal Defense Union Logistic Support
                60015090, # Covryn III - Federal Defense Union Logistic Support
                60015143, # Aidart IV - Federal Defense Union Logistic Support
                60015089, # Ostingele IV - Federal Defense Union Testing Facilities
                60015088, # Intaki II - Federal Defense Union Logistic Support
                60015085, # Eugales V - Federal Defense Union Assembly Plant
                60015086] # Moclinamaud VII - Federal Defense Union Logistic Support
        
        waypoints = [60010333] # Vlillirier VII - Roden Shipyards Factory
        for station_id in route:
            if systemlookup[station_id] in galmilsystems:
                waypoints.append(station_id)
        waypoints.append(30003836) # Vlillirier
        
        for waypoint in waypoints:
            self.SetWaypoint(waypoint)

if __name__ == '__main__':
    nav = FWMissionNavigator()
    nav.Authorize()
    nav.SetWaypoints()
