import requests


class MyClient():   
    def __init__(self, server_url):
        self.server_url = server_url
        cureent_response = None  
     
    def post_content(self, route, request_data):
        cureent_response = requests.post(self.server_url + route, 
                                         data = request_data)
        return cureent_response.json()
   
    def get_content(self, route):
        cureent_response = requests.get(self.server_url + route)
        return cureent_response.json()
    
    def get_cookie(self):
        return cureent_response.cookies    