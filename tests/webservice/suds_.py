# -*- coding: utf-8 -*-
from suds.client import Client
url = 'https://wsaa.afip.gov.ar/ws/services/LoginCms?wsdl'
client = Client(url)
print client
token = client.service.login()
print token
user = client.service.getUser(token, 'soaptester')
print user
