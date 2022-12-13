from pipelines_client import AzurePipelineClient
from utils import get_property, print_line_break

class AzurePipelineService():
    def __init__(self):
      self.pipelines_client = AzurePipelineClient()
    
    def get_pipelines_by_prop_with_initial_value_of(self, prop = 'name', name = 'disabled_'):
        all_pipelines = self.pipelines_client.get_pipelines();
        return filter(lambda pipe: pipe[prop].startswith(name), all_pipelines)
    
    def delete_pipelines_by_ids(self, pipelines_ids):
        print(pipelines_ids)
        builds_ids = self.__get_builds_ids_for_pipelines(pipelines_ids)
        print(f'Found {len(builds_ids)} builds to remove')
        
        for build_id in builds_ids:
            print_line_break()
            print(f'Removing build {build_id}')
            self.__delete_leases(build_id)
            # self.__delete_builds(build_id)   
        
    def __get_builds_ids_for_pipelines(self, pipelines_ids):
        return self.pipelines_client.get_builds_ids_for_pipelines(pipelines_ids)
        
    def __delete_leases(self, id):
        print(f'Retrieving leases for build {id}')
        leases = self.pipelines_client.get_leases_for_build(id)
        print(f'Found {len(leases)} leases for build {id}')
        
        if len(leases) == 0:
            return      
        
        leases_ids = get_property(leases, 'leaseId')                
        print(f'Deleting leases {leases_ids}')
        self.pipelines_client.delete_leases(leases_ids)
            
        print(f'Deleted all leases of {id}')
    
    def __delete_builds(self, id):
        self.pipelines_client.delete_build(id)
        