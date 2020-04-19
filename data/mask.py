import pprint
import requests
from bs4 import BeautifulSoup
import json
API_KEY = 'AIzaSyACHYbNNanITaj7X7-IxkJZ07l9vwhgD54'
url = f'https://www.googleapis.com/geolocation/v1/geolocate?key='+API_KEY
data = {
    'considerIp': True,
}

result = requests.post(url, data)
print(result.text)
#requests.get(result.text).json()
get_data = result.json()
list(get_data.keys())
geo_data = get_data.get('location')
geo_lat = geo_data.get('lat')
geo_lng = geo_data.get('lng')
str(geo_lat)
str(geo_lng)
print(geo_lat)                  #lat
print(geo_lng)                  #lng
print(get_data.get('accuracy')) #거리정확도

dist = str(3000)
mask_api = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat='+str(geo_lat)+'&lng='+str(geo_lng)+'&m='+str(dist)
print(mask_api)
