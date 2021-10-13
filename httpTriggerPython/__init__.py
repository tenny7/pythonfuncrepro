import logging
import os
import azure.functions as func
from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient


 
 
def tag_resources_in_resource_group(resource_group):
    resource_group = "ecommerce-dev-rg" 

    # subscription_id = os.environ.get(
    #     'AZURE_SUBSCRIPTION_ID',
    #     '795e5dad-6e94-41f8-af43-4321cd00cc8b') # your Azure Subscription Id
    subscription_id = '795e5dad-6e94-41f8-af43-4321cd00cc8b'
    credentials = ClientSecretCredential(
        client_id='e0e88edc-5e79-4438-ba66-743226c30ede',
        client_secret='Kbz7Q~LKkahniONFL0VQj63iz5-EJELyyWOM1',
        tenant_id='83230519-dce5-4e5a-91d7-17468e96478f'
    )
    resource_client = ResourceManagementClient(credentials, subscription_id)
    # resources = resource_client.resource_groups.list()
    # resources = resource_client.resources.list_by_resource_group(resource_group_name=resource_group)
    
    #print(resources)
    
    # for res in  resource_client.resource_groups.list_resources(resource_group):
    for res in resource_client.resource_groups.list():
        try:
            print(res)
            
            # res.tags.update({
            # 'BusinessFunctions' : resource_list.get(resource_group)[0],
            # 'BusinessVertical': resource_list.get(resource_group)[1]
            # })
            
            # print(resource_client.resources.begin_update_by_id(
            #     resource_id=res.id,
            #     api_version='2018-02-01',
            #     parameters=res))
        except Exception as e:
            print(e)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    tag_resources_in_resource_group("ecommerce-dev-rg")
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )	
  
        

