#!/usr/bin/python3

import json
import urllib.request


with open('wallet_addy.txt') as address_file:
	wallet_addy = address_file.read().rstrip()

hres = urllib.request.urlopen('https://api.opensea.io/api/v1/collections?asset_owner=' + wallet_addy + '&offset=0&limit=300')
jsondata = json.loads(hres.read().decode("utf-8"))

#print(json.dumps(jsondata, indent=4, sort_keys=True))

for data in jsondata:
	print("Name: ", data['name'], " | Floor Price: ", data['stats']['floor_price'], " | 1 Day Average: ", data['stats']['one_day_average_price'], " | 7 Day Average: ", data['stats']['seven_day_average_price'])

