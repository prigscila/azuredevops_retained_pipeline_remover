from dotenv import load_dotenv
from pipelines_client import AzurePipelineClient

def main():
    load_dotenv()
    pipelines_client = AzurePipelineClient()
    
    disabled_pipelines = list(pipelines_client.retrieve_disabled_pipelines())
    disabled_pipelines_ids = get_property(disabled_pipelines, 'id')
    disabled_pipelines_names = get_property(disabled_pipelines, 'name')
    disabled_pipelines_names.sort()
    
    display_disabled_pipelines(disabled_pipelines_names)
    should_continue = request_confirmation()
    
    if (should_continue):
        pipelines_client.delete_pipelines_by_ids(disabled_pipelines_ids)
        return
    
    print('No pipelines deleted, exiting...')    

def display_disabled_pipelines(disabled_pipelines_names):
    print(f'The following pipelines will be excluded: ')
    for pipeline in disabled_pipelines_names:
        print(pipeline)

def get_property(array, prop):
    return [ a[prop] for a in array ]

def request_confirmation():
    print('Proceed with pipelines exclusion? [y/n]')
    user_input = input()
    return user_input == 'y'

if __name__ == "__main__":
    main()