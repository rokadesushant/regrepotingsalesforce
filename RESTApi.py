import requests
import base64
import json

params = {
    "grant_type":"password",
    "client_id":"3MVG9fe4g9fhX0E70nZ5ND5mX83mESuQiw8EZeH2hXMRs_Ipgj5OKjFp5FVukSeig71uiG7Lg.e3Jk06iy8Ob",
    "client_secret":"1F49F29A9CC013C311FC32543D8EE7CDFAFE39580BAB65C84000A2548787B326",
    "username":"serverorgintegration@gmail.com",
    "password":"sushant@7",
}

r = requests.post("https://login.salesforce.com/services/oauth2/token",data=params);
print(r)
access_token = r.json().get("access_token")
instance_url = r.json().get("instance_url")

print("Access Token ",access_token)
print("Instance url ",instance_url)

def sf_call(action,parameters={},method='get',data={}):
    headers = {
        'Content_type':'application/json',
        'Accept_Encoding':'gzip',
        'Authorization':'Bearer%s'%access_token
    }

    if method=='get':
        r = requests(method,instance_url+action,headers=headers,params=parameters,timeout=30)
    elif method in ['post','patch']:
        r = requests(method, instance_url + action, headers=headers, json=data , params=parameters, timeout=10)
    else:
        raise ValueError('Method should be either get or post or patch')

    if r.status_code<300:
        if method=='patch':
            return None
        else:
            return r.json()
    else:
        return Exception('Api error when calling URL')

opportunity_data = json.dumps(sf_call('/services/data/v45.0/query/',{'q':'SELECT id,Name,ClosedDate from Opportunity'}),indent=2)

print(opportunity_data)
