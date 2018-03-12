'''
1) [ESI] Retrieve list of FW systems
2) For each system in the default route:
	If the system is Gallente-controlled on the FW system list:
		Add that system as a waypoint
		
		
		
		
		
Gallente militia faction ID: 500004

		 
		 
 https://developers.eveonline.com/blog/article/sso-to-authenticated-calls
 https://docs.google.com/document/d/19yQK9uOlxi5dFWZa60Zeoao6ivPwLX_BnU4X-9vOIL8/edit

'''


import requests

client_id = ''
clientToken = ''
scopes = ('')


class FWMissionNavigator():
		
	def Authorize(self):
		sso_url = 'https://login.eveonline.com/oauth/authorize/?response_type=code'
		sso_url += '&client_id=' + self.clientID
		sso_url += '&redirect_uri=http://127.0.0.1:8000'
		sso_url += '&scope=' + scopes
		
		# ETC
		# ETC
		# ETC
	
	def SetWaypoint(self, destination_id, clear_outherwaypoints=False):
		url = 'https://esi.tech.ccp.is/latest/ui/autopilot/waypoint/'
		url += '?add_to_beginning=false'
		url += '&clear_otherwaypoints=%s' % clear_otherwaypoints
		url += '&datasource=tranquility'
		url += '&destination_id=%s' % destination_id
	
	def SetWaypoints(self):
		fwsystems = requests.get('https://esi.tech.ccp.is/latest/fw/systems/?datasource=tranquility')
		
		route = [60010333, # Vlillirier VII - Roden Shipyards Factory
				60015084, # Esesier IX - Federal Defense Union Logistic Support
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
				60015086, # Moclinamaud VII - Federal Defense Union Logistic Support
				60010333] # Vlillirier VII - Roden Shipyards Factory
		
		for 




		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
