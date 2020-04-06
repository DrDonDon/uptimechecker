# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:25:08 2020

@author: Isaac
"""

from dotenv import load_dotenv
load_dotenv()
 
import requests
import time
from datetime import datetime
import os
from amphora.client import AmphoraDataRepositoryClient, Credentials
import amphora_api_client as a10a
from amphora_api_client.rest import ApiException
from amphora_api_client.configuration import Configuration
import pandas as pd
import numpy as np

ad_url = "https://beta.amphoradata.com/healthz"
id = "a6f2a8b4-0c72-402e-b820-90aedecea14f"

def get_isup():
    r = requests.get(ad_url)
    return (r.status_code == 200 and len(r.content) == 7)

isup_status = get_isup()

if (isup_status):
    print("It's up!")
else:
    print("It ain't up")

credentials = Credentials(username=os.getenv('username'), password=os.getenv('password'))
client = AmphoraDataRepositoryClient(credentials)


#try:
    # Gets a token
    #res = auth_api.authentication_request_token(token_request = token_request)
    #configuration.api_key["Authorization"] = "Bearer " + res
    # create an instance of the Users API, now with Bearer token
    #users_api = amphora_client.UsersApi(amphora_client.ApiClient(configuration))
    #me = users_api.users_read_self()
    #print(me)
#except ApiException as e:
#    print("Exception when calling AuthenticationAPI: %s\n" % e)

amphora_api = a10a.AmphoraeApi(client.apiClient)
amphora = client.get_amphora(id ) 

Signal = []
try:
    if (isup_status):
        Signal.append(dict(t = datetime.utcnow(),isup = 1))
    else:
        Signal.append(dict(t = datetime.utcnow(),isup = 0))
    amphora.push_signals_dict_array(Signal)  
except ApiException as e:
    print("Exception when calling AmphoraeApi: %s\n" % e)
