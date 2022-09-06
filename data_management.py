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

#create object instance
Account = SFType('Account',session_id,instance)

"""
data = {
    'Name':'Sushant Rokade Python',
    'Industry':'Agriculture',
    'Rating':'Hot'
}

response = Account.create(data)

print(response)

account = SFType('Account',session_id,instance)
Contact = SFType('Contact',session_id,instance)

for i in range(1,6):
    data_account = {
        'Name':'Retail Account '+str(i),
        'Industry': 'Agriculture',
        'Rating': 'Hot'
    }
    response_account = account.create(data_account)
    accountId = response_account.get('id')

    data_contact = {
        'FirstName':'Sushant '+str(i),
        'LastName':'Rokade',
        'AccountId':accountId
    }

    response_contact = Contact.create(data_contact)
    contactId = response_contact.get('id')

    print('Record Created')
    print('-'.center(50,'-'))
    print('Account Id: {0}'.format(accountId))
    print('Contact Id: {0}'.format(contactId))
"""
#update records

update_data = {}
update_data['Name'] = 'Retail 1 updated'
#update_data['Id'] = '0015g00000qHJ5fAAG'

Account.update('0015g00000qHJ5fAAG',update_data)

#upsert records

externam_Id = 'Ext_Id__c/{0}'.format('external Id')

response = Account.upsert(externam_Id,data=update_data);
