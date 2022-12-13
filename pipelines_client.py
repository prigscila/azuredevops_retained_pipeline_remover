import os
import requests
import json
from auth import get_authorization_header
from utils import get_property

class AzurePipelineClient():
    def __init__(self):
      self.baseUrl = os.getenv('AZURE_PROJECT_URL')
      self.user = os.getenv('USER')
      self.pat = os.getenv('PAT')
      self.api_version = os.getenv('API_VERSION')
    
    def get_pipelines(self):
        headers = get_authorization_header(self.user, self.pat)       
        params = self.__get_default_params()
        url = f'{self.baseUrl}/_apis/pipelines'
        
        response = requests.get(url, headers=headers, params=params)
        pipelines_content = json.loads(response.text)
        
        return pipelines_content['value']
    
    def get_builds_ids_for_pipelines(self, pipelines_ids):
        headers = get_authorization_header(self.user, self.pat)       
        params = { 
            'api-version': self.api_version,
            'definitions': self.__get_comma_separated_ids(pipelines_ids)
        }
        
        url = f'{self.baseUrl}/_apis/build/builds'
        
        response = requests.get(url, params=params, headers=headers)
        builds_content = json.loads(response.text)
        all_builds = builds_content['value']
        
        return get_property(all_builds, 'id')

    def __get_comma_separated_ids(self, pipelines_ids):
        return ','.join([str(i) for i in pipelines_ids])
    
    def get_leases_for_build(self, id):
        headers = get_authorization_header(self.user, self.pat)       
        params = self.__get_default_params()        
        url = f'{self.baseUrl}/_apis/build/builds/{id}/leases'

        response = requests.get(url, params=params, headers=headers)
        leases_content = json.loads(response.text)
        return leases_content['value']
    
    def delete_leases(self, ids):
        headers = get_authorization_header(self.user, self.pat)       
        params = { 
            'api-version': self.api_version,
            'ids': self.__get_comma_separated_ids(ids)
        }
        url = f'{self.baseUrl}/_apis/build/retention/leases'
        requests.delete(url, params=params, headers=headers)
            
    def delete_build(self, id):
        headers = get_authorization_header(self.user, self.pat)       
        params = self.__get_default_params()
        url = f'{self.baseUrl}/_apis/build/builds/{id}'
        requests.delete(url, params=params, headers=headers)
        
    def __get_default_params(self):
        return { 'api-version': self.api_version }