import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from data import token

API_KEY = token.API_KEY
url = f'https://www.googleapis.com/geolocation/v1/geolocate?key='+API_KEY
#data = {
#    'considerIp': True,
#}

result = requests.post(url)
print(result.text)
#requests.get(result.text).json()
get_data = result.json()
list(get_data.keys())
geo_data = get_data.get('location')
geo_lat = geo_data.get('lat')   #lat
geo_lng = geo_data.get('lng')   #lng
accu = get_data.get('accuracy') #거리정확도

dist = str(1000)
mask_api = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByGeo/json?lat='+str(geo_lat)+'&lng='+str(geo_lng)+'&m='+str(dist)
print(mask_api)

get_mask = requests.get(mask_api)
mask_all = get_mask.json()
list(mask_all.keys())
store_count = mask_all['count']
mask_info = mask_all['stores']
print(mask_info)
all_store = mask_info[5]
all_addr = mask_info[0]
remain_mask = mask_info[6]
stock = mask_info[7]
lat= mask_info[3]
lng= mask_info[4]
#type= mask_info[8]
#print(all_store)
#print(all_addr)
#print(remain_mask)
#print(stock)
#print(type)

i=0;
mark = []
for i in range(int(store_count)+1):
    if i == store_count :
        print('mask info end')
        continue
    print(mask_info[i])
    all_store = mask_info[i]
    all_addr = mask_info[i]
    remain_mask = mask_info[i]
    stock = mask_info[i]
    lat= mask_info[i]
    lng= mask_info[i]
#    type = mask_info[i]

    location = str(lat['lat']) + ',' + str(lng['lng'])
    mark.append(location)
    print(mark)


    print(store_count)
    print('=========')
    print(all_store['name'])                    #판매처 이름
    print('=========')
    print(all_addr['addr'])                     #판매처 주소
    print('=========')
    print(remain_mask['remain_stat'])           #재고 상태 100개이상(녹색)=plenty, 30개이상 100개미만(노랑색)=some,
    print('=========')                          #2개이상 30개미만(빨강색)=few, 1개이하(회색)=empty, 판매중지=break
    print(stock['stock_at'])                    #입고시간
    print('=========')
    print(location)                             #위도,경도
    print('=========')
#    print(type['type'])                         #판매처 유형 01=약국, 02=우체국, 03=농협
    print('=========')
marker = []
print(mark)
for i in range (1,int(store_count)):
    loop_m = '&markers='+str(mark[i])
    marker.append(loop_m+str(i))
    if i == store_count:
        continue
    print(marker)
    print(i)

#if (mask_info[8]==int(0o1)):
#    print(shop[0])
#    print(mask_info[8])
#elif mask_info[8]== int(0o2):
#    print(shop[1])
#    print(mask_info[8])
#elif mask_info[8]== int(0o3):
#    print(shop[2])
#    print(mask_info[8])

#marker = '&markers=color:blue'+'%7C'+str(location)
#print(marker)

#all_store = mask_info['name'][i]
#all_addr = mask_info['addr'][i]
#remain_mask = mask_info['remain_stat'][i]
#stock = mask_info['stock_at'][i]
#print(all_store)
#print(all_addr)
#print(remain_mask)
#print(stock)

d = ['월', '화', '수', '목', '금', '토', '일']
y = datetime.today().weekday()
print(d[y])
if y == 0:
    buy_mask = '주민번호 끝자리 1,6년생'
elif y == 1:
    buy_mask = '주민번호 끝자리 2,7년생'
elif y == 2:
    buy_mask = '주민번호 끝자리 3,8년생'
elif y == 3:
    buy_mask = '주민번호 끝자리 4,9년생'
elif y == 4:
    buy_mask = '주민번호 끝자리 5,0년생'
elif y == 5:
    buy_mask = '모든사람'
elif y == 6:
    buy_mask = '모든사람'


#maps_url =  'https://maps.googleapis.com/maps/api/directions/json?origin='+str(geo_lat)+','+str(geo_lng)+'&key='+map_api
maps_url = 'https://maps.googleapis.com/maps/api/staticmap?center='+str(geo_lat)+','+str(geo_lng)+'&zoom=15&size=600x600&maptype=roadmap&region=kr&format=png'+str(''.join(marker))+'&key='+API_KEY
print(maps_url)
