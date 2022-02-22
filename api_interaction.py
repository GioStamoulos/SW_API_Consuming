import json
import requests as rq
from collections import defaultdict as dfd

class api_interaction:

    def __init__(self,api):
        self.api = api


    def api_connect(self):
        #connect with api
        response_API = rq.get(self.api)
        return response_API.json()
        
    def create_result_dict(self, api_json):
        result_dict = api_json['results']
        conc_dict= dfd(list)
        for i in result_dict:
            for j in i:
                conc_dict[j].append(i[j])
        return conc_dict
            