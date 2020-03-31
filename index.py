from dotenv import load_dotenv
load_dotenv()

import requests
import time
import os
from amphora.client import AmphoraDataRepositoryClient, Credentials
import amphora_api_client as a10a
from amphora_api_client.rest import ApiException
from amphora_api_client.configuration import Configuration

ad_url = "https://beta.amphoradata.com/healthz"
id = "a6f2a8b4-0c72-402e-b820-90aedecea14f"

def get_isup():
    r = requests.get(ad_url)
    return (r.status_code == 200 and len(r.content) == 0)

isup_status = get_isup()

if (isup_status):
    print("It's up!")
else:
    print("It ain't up")

# Set up connection to amphoradata.com
# provide your login credentials
credentials = Credentials(username=os.getenv('username'), password=os.getenv('password'))
# create a client for interacting with the public Amphora Data Repository
client = AmphoraDataRepositoryClient(credentials)

try:
    # Gets a token
    # create an instance of the Users API, now with Bearer token
    users_api = amphora_client.UsersApi(amphora_client.ApiClient(configuration))
    me = users_api.users_read_self()
    print(me)
except ApiException as e:
    print("Exception when calling AuthenticationAPI: %s\n" % e)

amphora_api = a10a.AmphoraeApi(client.apiClient)

try:
    if (isup_status):
        s = {'isup': 1}
    else:
        s = {'isup': 0}
    amphora_api.push_signals_dict_array(request_body=s)
except ApiException as e:
    print("Exception when calling AmphoraeApi: %s\n" % e)
