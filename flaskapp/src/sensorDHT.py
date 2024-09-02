import requests
import time

class SensorDht:
    def __init__(self, url, port, endpoints):
        self.url = url
        self.port = port
        self.endpoints = endpoints

    def get_endpoint(self, endpoint):
        try:
            req = requests.get(f'{self.url}:{self.port}/{endpoint}')
            req.raise_for_status()  
            return req.json()
        except requests.RequestException as e:
            return {'error': str(e)}  

    def request_endpoint(self, endpoint, timeit=False):
        if timeit:
            start = time.time()
            req = self.get_endpoint(endpoint=endpoint)
            dur = time.time() - start
            return req, dur
        else:
            req = self.get_endpoint(endpoint=endpoint)
            return req
