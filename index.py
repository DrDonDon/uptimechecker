from dotenv import load_dotenv
load_dotenv()
 
import requests
import time
import os
import amphora_client
from amphora_client.rest import ApiException
from amphora_client.configuration import Configuration

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

configuration = Configuration()
auth_api = amphora_client.AuthenticationApi(amphora_client.ApiClient(configuration))
token_request = amphora_client.TokenRequest(username=os.getenv('username'), password=os.getenv('password') )

try:
    # Gets a token
    res = auth_api.authentication_request_token(token_request = token_request)
    configuration.api_key["Authorization"] = "Bearer " + res
    # create an instance of the Users API, now with Bearer token
    users_api = amphora_client.UsersApi(amphora_client.ApiClient(configuration))
    me = users_api.users_read_self()
    print(me)
except ApiException as e:
    print("Exception when calling AuthenticationAPI: %s\n" % e)

amphora_api = amphora_client.AmphoraeApi(amphora_client.ApiClient(configuration))

try:
    if (isup_status):
        s = {'isup': 1}
    else:
        s = {'isup': 0}
    amphora_api.amphorae_signals_upload_signal(id, request_body=s)
except ApiException as e:
    print("Exception when calling AmphoraeApi: %s\n" % e)
