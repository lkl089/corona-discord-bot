import requests
import json
API_KEY = 'AIzaSyACHYbNNanITaj7X7-IxkJZ07l9vwhgD54'
url = f'https://www.googleapis.com/geolocation/v1/geolocate?key='+API_KEY
data = {
    'considerIp': True,

}

result = requests.post(url, data)
print(result.text)
#requests.get(result.text).json()
geo_data = result.json()
list(geo_data)
print(geo_data)
#lat = geo_data['lat']
#lng = geo_data['lng']
dist = 3000
#mask_api = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat='+lat+'&lng='+lng+'&m='+dist

