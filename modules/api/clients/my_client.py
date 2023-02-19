import requests


class MyClient(): 

    def __init__(self, server_url):
        self.server_url = server_url
        self.cureent_response = None
    
    def post_content(self, route, request_data, cookie=None):
        self.cureent_response = requests.post(self.server_url + route,
                                         data=request_data, cookies=cookie)
        return self.cureent_response.json()
   
    def get_content(self, route, cookie=None):
        self.cureent_response = requests.get(self.server_url + route, cookies=cookie)
        return self.cureent_response.json()
    
    def get_cookies(self):
        return self.cureent_response.cookies
    
    def get_headers(self):
        return dict(self.cureent_response.headers)
    
    def get_file(self, route, cookie=None):
        self.cureent_response = requests.get(self.server_url + route, cookies=cookie)
        return self.cureent_response
