import os
import requests
import json
from auth import get_authorization_header

class AzurePipelineClient():
    def __init__(self):
      self.organization = os.getenv('ORGANIZATION')
      self.project = os.getenv('PROJECT')
      self.user = os.getenv('USER')
      self.pat = os.getenv('PAT')
      self.baseUrl = os.getenv('BASE_URL')
    
    def retrieve_disabled_pipelines(self):
        headers = get_authorization_header(self.user, self.pat)
        params = { 'api-version': '7.0' }

        url = f'{self.baseUrl}/{self.organization}/{self.project}/_apis/pipelines?api-version=7.0'
        response = requests.get(url, headers=headers, params=params)

        pipelines_content = json.loads(response.text)
        all_pipelines = pipelines_content['value']

        return filter(lambda pipe: pipe['name'].startswith('disabled'), all_pipelines)
    
    def delete_pipelines_by_ids(self, ids):
        print()