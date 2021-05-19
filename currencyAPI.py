import requests
import json

baseUrl = 'https://prime.exchangerate-api.com/v5/6e106a9454d9f4a1696d1d95/latest/USD'
response = requests.get(baseUrl)
data = response.json()
randPrice = data['conversion_rates']

print("$1 United States Dollar = R%s South African Rand" % (randPrice['ZAR']))

