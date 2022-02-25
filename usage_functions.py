from urllib import response
import requests
import datetime
import pandas as pd
import json

#YYYY-MM-DD[T]HH:mm:ss (SGT)
#trying to figure out how to work with the usage of the API


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

today = datetime.datetime.today()
params = {"data" : today.strftime("%Y-%m-%d") +"T" + today.strftime("%H:%M:%S")} # YYYY-MM-DD

print(params)

response = requests.get('https://api.data.gov.sg/v1/transport/carpark-availability',params = params)
data = response.json()

if response.status_code == 200:
    print("Data received successfully")
else:
    print(response.status_code)
    print("Error")
