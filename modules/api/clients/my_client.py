import requests


class MyClient():   
    def __init__(self, server_url):
        self.server_url = server_url
        self.cureent_response = None
    
    def post_content(self, route, request_data):
        self.cureent_response = requests.post(self.server_url + route, 
                                         data = request_data)
        return self.cureent_response.json()
   
    def get_content(self, route):
        self.cureent_response = requests.get(self.server_url + route)
        return self.cureent_response.json()
    
    def get_cookies(self):
        return self.cureent_response.cookies    