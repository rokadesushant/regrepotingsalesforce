import json
import pandas
import pandas as pd
from simple_salesforce import Salesforce, SalesforceLogin, SFType

username = 'serverorgintegration@gmail.com'
password = 'sushant@7'
security_token = 'mwWqHIkaMGFwrfZCPb83mwOvm'
domain = 'login'

session_id, instance = SalesforceLogin(username=username,password=password,security_token=security_token,domain=domain)

sf = Salesforce(instance=instance,session_id=session_id)

values = ['Energy','Banking']

#querySOQL = """SELECT ID,Name,Type,Industry FROM Account WHERE Industry IN('{0}')""".format("',".join(values))
querySOQL = """SELECT ID,Name,Type,Industry FROM Account"""
#recordsAccount = sf.query(querySOQL)

response = sf.query(querySOQL)

lstRecords = response.get('records')
nextRecordsUrl = response.get('nextRecordsUrl')

while not response.get('done'):
    response = sf.query_more(nextRecordsUrl,identifier_is_url=true)
    lstRecords.extend(response.get('records'))
    nextRecordsUrl = response.get('nextRecordsUrl')

print(lstRecords)

df = pd.DataFrame(lstRecords)
print(df)

#print(recordsAccount)