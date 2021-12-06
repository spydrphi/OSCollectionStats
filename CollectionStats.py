#!/usr/bin/python3

import json
import urllib.request
import urllib.parse

with open('wallet_addy.txt') as address_file:
	wallet_addy = address_file.read().rstrip()
	
with open('api_key.txt') as key_file:
	api_key = key_file.read().rstrip()

url = 'https://api.opensea.io/api/v1/collections?asset_owner=' + wallet_addy + '&offset=0&limit=300'
headers = {'x-api-key': '{key}'.format(key=api_key)}

req = urllib.request.Request(url, data=None, headers=headers)
hres = urllib.request.urlopen(req)

jsondata = json.loads(hres.read().decode("utf-8"))

#debug statement, uncomment if needed
#print(json.dumps(jsondata, indent=4, sort_keys=True))

for data in jsondata:
	print("Name: ", data['name'], " | Floor Price: ", data['stats']['floor_price'], " | 1 Day Average: ", data['stats']['one_day_average_price'], " | 7 Day Average: ", data['stats']['seven_day_average_price'])

