from dotenv import load_dotenv
from pipelines_service import AzurePipelineService
from utils import get_property

def main():
    load_dotenv()
    pipelines_service = AzurePipelineService()
    
    # prop = get_prop_to_filter_by()
    # value = get_prop_value_to_filter_by()    
    
    pipelines = list(pipelines_service.get_pipelines_by_prop_with_initial_value_of())
    pipelines_ids = get_property(pipelines, 'id')
    pipelines_names = get_property(pipelines, 'name')
    pipelines_names.sort()
    
    display_retrieved_pipelines(pipelines_names)
    should_continue_with_exclusion = request_confirmation()
    
    if should_continue_with_exclusion:
        pipelines_service.delete_pipelines_by_ids(pipelines_ids)
        return
    
    print('No pipelines deleted, exiting...')    

def get_prop_to_filter_by():
    print('Which property should the pipelines be filtered by?')
    return request_user_input()

def get_prop_value_to_filter_by():
    print('Which value should be used to filter this property?')
    return request_user_input()

def request_user_input():
    user_input = input()
    if not user_input:
        return None
    return user_input

def display_retrieved_pipelines(disabled_pipelines_names):
    print(f'The following pipelines will be excluded: ')
    for pipeline in disabled_pipelines_names:
        print(pipeline)

def request_confirmation():
    print('Proceed with pipelines exclusion? [y/n]')
    user_input = input()
    return user_input == 'y'

if __name__ == "__main__":
    main()