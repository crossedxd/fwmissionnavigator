import webbrowser

import requests
from eveauth import Auth


class FWMissionNavigator():

    def __init__(self):
        self.session = Auth().session()

        self.systemlookup = {60010333: 30003836,
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

        self.route = [60015084,  # Esesier IX
                      60015087,  # Mercomesier III
                      60015145,  # Orvolle VII
                      60015142,  # Caslemon III
                      60015144,  # Villore VI
                      60015081,  # Parts I
                      60015080,  # Fliet III
                      60015082,  # Costolle V
                      60015092,  # Jufvitte IV
                      60015083,  # Ouelletta II
                      60015091,  # Uphallant II
                      60015090,  # Covryn III
                      60015143,  # Aidart IV
                      60015089,  # Ostingele IV
                      60015088,  # Intaki II
                      60015085,  # Eugales V
                      60015086]  # Moclinamaud VII

    def set_waypoint(self, destination_id):
        wp_url = ('https://esi.evetech.net/latest/'
                  'ui/autopilot/waypoint/?'
                  'add_to_beginning=false&'
                  'clear_other_waypoints=false&'
                  'datasource=tranquility&'
                  'destination_id={}'.format(destination_id))
        self.session.post(wp_url)

    def set_waypoints(self):
        sys_url = ('https://esi.evetech.net/latest/'
                   'fw/systems/?datasource=tranquility')
        systems = [system['solar_system_id'] for system in
                   self.session.get(sys_url).json()
                   if system['occupier_faction_id'] == 500004]
        waypoints = [60010333]  # Vlillirier VII
        for station_id in self.route:
            if self.systemlookup[station_id] in systems:
                waypoints.append(station_id)
        waypoints.append(30003836)  # Vlillirier
        for waypoint in waypoints:
            self.set_waypoint(waypoint)


if __name__ == '__main__':
    FWMissionNavigator().set_waypoints()
