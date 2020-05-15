from bs4 import BeautifulSoup
from urllib.request import Request
import urllib.error
import requests

#base_url = 'https://raw.githubusercontent.com/CSSEGISandData/2019-nCoV/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-%s.csv';
#base_url ='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/'+month+'-'+day+'-'+year+'-'+'.csv'
#worldometers
headers = {'User-Agent':'Chrome/81.0.4044.92'}
w_url = 'https://www.worldometers.info/coronavirus/'
w_req = Request(w_url, headers=headers)

w_html = urllib.request.urlopen(w_req).read()
w_soup = BeautifulSoup(w_html, 'html.parser')

#Total값 찾기
w_table = w_soup.find_all('tr', {'class': 'total_row'})
print(w_table)
#total_row중 8번째값 (실 토탈값)
w_c = w_table[7]
print("=======")
print(w_c)
w_tds = w_c.find_all('td')
print("=======")

#전세계 확진자
w_confirmed = w_tds[1].text.strip()
print(w_confirmed)

#전일대비 증가
w_prev_confirmed = w_tds[2].text.strip()
w_prev_confirmed = w_prev_confirmed.replace("+","")
print(w_prev_confirmed)

#전세계 사망자
w_death = w_tds[3].text.strip()
print(w_death)

#전일대비 증가
w_prev_death = w_tds[4].text.strip()
w_prev_death = w_prev_death.replace("+","")
print(w_prev_death)

#전세계 완치자
w_rescued = w_tds[5].text.strip()
print(w_rescued)

#전세계 치료중인자
w_active = w_tds[6].text.strip()
print(w_active)
print("world end")
print("=======")

#미국
usa = w_soup.find_all('tr')
usa_all = usa[9]
usa_all = usa_all.find_all('td')
usa_confim = usa_all[1].text.strip()
usa_prev_confim = usa_all[2].text.strip()
usa_prev_confim = usa_prev_confim.replace("+","")
usa_dead = usa_all[3].text.strip()
usa_prev_dead = usa_all[4].text.strip()
usa_prev_dead = usa_prev_dead.replace("+","")
usa_resued = usa_all[5].text.strip()
usa_active = usa_all[6].text.strip()

print(usa)
print('here!!!')
print(len(usa))
print(usa_all)
print(usa_confim)
print(usa_prev_confim)
print(usa_dead)
print(usa_prev_dead)
print(usa_resued)
print(usa_active)
#print(usa_confim)



##대륙별
#아시아
print("asia start")
print("=======")
as_c = w_table[2]
print("=======")
print(as_c)
as_tds = as_c.find_all('td')
print("=======")

#아시아 확진자
as_confirmed = as_tds[1].text.strip()
print(as_confirmed)

#전일대비 증가
as_prev_confirmed = as_tds[2].text.strip()
as_prev_confirmed = as_prev_confirmed.replace("+","")
print(as_prev_confirmed)

#아시아 사망자
as_death = as_tds[3].text.strip()
print(as_death)

#전일대비 증가
as_prev_death = as_tds[4].text.strip()
as_prev_death = as_prev_death.replace("+","")
print(as_prev_death)

#아시아 완치자
as_rescued = as_tds[5].text.strip()
print(as_rescued)

#아시아 치료중인자
as_active = as_tds[6].text.strip()
print(as_active)
print("asia end")
print("=======")
#유럽
print("europe start")
print("=======")
eu_c = w_table[1]
print("=======")
print(eu_c)
eu_tds = eu_c.find_all('td')
print("=======")

#유럽 확진자
eu_confirmed = eu_tds[1].text.strip()
print(eu_confirmed)

#전일대비 증가
eu_prev_confirmed = eu_tds[2].text.strip()
eu_prev_confirmed = eu_prev_confirmed.replace("+","")
print(eu_prev_confirmed)

#유럽 사망자
eu_death = eu_tds[3].text.strip()
print(eu_death)

#전일대비 증가
eu_prev_death = eu_tds[4].text.strip()
eu_prev_death = eu_prev_death.replace("+","")
print(w_prev_death)

#유럽 완치자
eu_rescued = eu_tds[5].text.strip()
print(eu_rescued)

#유럽 치료중인자
eu_active = eu_tds[6].text.strip()
print(eu_active)
print("europe end")
print("=======")

#북아메리카
print("north america start")
print("=======")
na_c = w_table[0]
print("=======")
print(na_c)
na_tds = na_c.find_all('td')
print("=======")

#북아메리카 확진자
na_confirmed = na_tds[1].text.strip()
print(na_confirmed)

#전일대비 증가
na_prev_confirmed = na_tds[2].text.strip()
na_prev_confirmed = na_prev_confirmed.replace("+","")
print(na_prev_confirmed)

#북아메리카 사망자
na_death = na_tds[3].text.strip()
print(na_death)

#전일대비 증가
na_prev_death = na_tds[4].text.strip()
na_prev_death = na_prev_death.replace("+","")
print(na_prev_death)

#북아메리카 완치자
na_rescued = na_tds[5].text.strip()
print(na_rescued)

#북아메리카 치료중인자
na_active = na_tds[6].text.strip()
print(na_active)
print("north america end")
print("=======")

#남아메리카
print("south america start")
print("=======")
sa_c = w_table[3]
print("=======")
print(sa_c)
sa_tds = sa_c.find_all('td')
print("=======")

#남아메리카 확진자
sa_confirmed = sa_tds[1].text.strip()
print(sa_confirmed)

#전일대비 증가
sa_prev_confirmed = sa_tds[2].text.strip()
sa_prev_confirmed = sa_prev_confirmed.replace("+","")
print(sa_prev_confirmed)

#남아메리카 사망자
sa_death = sa_tds[3].text.strip()
print(sa_death)

#전일대비 증가
sa_prev_death = sa_tds[4].text.strip()
sa_prev_death = sa_prev_death.replace("+","")
print(sa_prev_death)

#남아메리카 완치자
sa_rescued = sa_tds[5].text.strip()
print(sa_rescued)

#남아메리카 치료중인자
sa_active = sa_tds[6].text.strip()
print(sa_active)
print("south america end")
print("=======")

#아프리카
print("africa start")
print("=======")
af_c = w_table[5]
print("=======")
print(af_c)
af_tds = af_c.find_all('td')
print("=======")

#아프리카 확진자
af_confirmed = af_tds[1].text.strip()
print(af_confirmed)

#전일대비 증가
af_prev_confirmed = af_tds[2].text.strip()
af_prev_confirmed = af_prev_confirmed.replace("+","")
print(af_prev_confirmed)

#아프리카 사망자
af_death = af_tds[3].text.strip()
print(w_death)

#전일대비 증가
af_prev_death = af_tds[4].text.strip()
af_prev_death = af_prev_death.replace("+","")
print(w_prev_death)

#아프리카 완치자
af_rescued = af_tds[5].text.strip()
print(af_rescued)

#아프리카 치료중인자
af_active = af_tds[6].text.strip()
print(af_active)
print("africa end")
print("=======")

#오세아니아
print("oceania start")
print("=======")
oc_c = w_table[4]
print("=======")
print(oc_c)
oc_tds = oc_c.find_all('td')
print("=======")

#오세아니아 확진자
oc_confirmed = oc_tds[1].text.strip()
print(oc_confirmed)

#전일대비 증가
oc_prev_confirmed = oc_tds[2].text.strip()
oc_prev_confirmed = oc_prev_confirmed.replace("+","")
print(oc_prev_confirmed)

#오세아니아 사망자
oc_death = oc_tds[3].text.strip()
print(oc_death)

#전일대비 증가
oc_prev_death = oc_tds[4].text.strip()
oc_prev_death = oc_prev_death.replace("+","")
print(oc_prev_death)

#오세아니아 완치자
oc_rescued = oc_tds[5].text.strip()
print(w_rescued)

#오세아니아 치료중인자
oc_active = oc_tds[6].text.strip()
print(oc_active)
print("oceania end")
print("=======")


#print(base_url)
#response = requests.get(base_url)
#file = csv.reader(response.text.strip().split('\n'))
#for record in file:
#        if record[0] != 'year':
#            Confirmed = int(record[0])
#           Deaths = int(record[1])
#           Recovered = int(record[2])
#
#           print(Confirmed, Deaths, Recovered)
