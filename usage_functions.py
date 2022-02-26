import requests
import datetime
import pandas as pd

#YYYY-MM-DD[T]HH:mm:ss (SGT)
#trying to figure out how to work with the usage of the API

today = datetime.datetime.today()
params = {"data" : today.strftime("%Y-%m-%d") +"T" + today.strftime("%H:%M:%S")} # YYYY-MM-DD

x = requests.get('https://api.data.gov.sg/v1/transport/carpark-availability',params = params).json()

print(x.json.keys())