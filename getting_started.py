import json
import pandas
from simple_salesforce import Salesforce, SalesforceLogin, SFType

username = 'serverorgintegration@gmail.com'
password = 'sushant@7'
security_token = 'mwWqHIkaMGFwrfZCPb83mwOvm'
domain = 'login'
#sf =Salesforce(username=username,password=password,security_token=security_token,domain=domain)

session_id, instance = SalesforceLogin(username=username,password=password,security_token=security_token,domain=domain)

sf = Salesforce(instance=instance,session_id=session_id)

print(sf)

#for element in dir(sf):
   # if not element.startswith('_'):
      #  print('Property Name:{0} ; Value: {1}'.format(element,getattr(sf,element)))

metadata_org = sf.describe()

print(metadata_org)

print()