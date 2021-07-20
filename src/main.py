import requests
import csv
from src.auth import auth as authentication
from pprint import pprint
import json

site_url = 'https://step2.test/'
rest_path = 'rest/default/V1/'
sku = 'testsku1'

endpoint = f"{site_url}{rest_path}products/{sku}"
auth = authentication.get_auth()

print(endpoint)

try:
    response = requests.get(endpoint, auth=auth, verify=False)
    pprint(json.loads(response.content.decode()))
except Exception as e:
    print("There was one of them errors")
    print(e)
