#make a program that generate random quotes from using quotes api
import enum
import requests
import json

url = "https://type.fit/api/quotes"
response = requests.get(url)
data = json.loads(response.text)

import random
for a,b in enumerate(data):
   

   print(data[a]["text"])