# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import Request
import urllib.error
from data import world_data
import requests

#mhow
url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
#print(soup)

#사망자 정보
url2 = "http://ncov.mohw.go.kr/"
html2 = urllib.request.urlopen(url2).read()
soup2 = BeautifulSoup(html2, 'html.parser')
#print(soup2)

#coronaboard (임시)
headers = {'User-Agent':'Chrome/81.0.4044.92'}
url3 = "https://coronaboard.kr/"
req = Request(url3, headers=headers)
#html3 = urllib.request.urlopen(req).read()
html3 = urllib.request.urlopen(req)
#soup3 = BeautifulSoup(html3, 'html.parser')
soup3 = BeautifulSoup(html3, 'html.parser')
#print(soup3)

#한국 확진자,격리해제,격리자,사망자 정보 가져오기
table = soup.find('table', {'class': 'num'})
#print(table)
tds = table.find_all('td')
confirmed = tds[0].text.strip()
rescued = tds[1].text.strip()
cure = tds[2].text.strip()
dead = tds[3].text.strip()

#전일대비 확진자 증가수
table_c = soup.find('div', {'class': 'hdn'})
#print(table_c)
tds_c = table_c.find_all('td')
prev_confimed = tds_c[20].text.strip()
#print(prev_confimed)

#전일대비 격리해제 증가수
table_r = soup.find_all('div', {'class': 'hdn'})
#print(table_r)
tds_r = table_r[1].find_all('td')
prev_rescured = tds_r[20].text.strip()
#print(prev_rescured)

#누적 검사 완료수
table_total_test = soup.find_all('div', {'class': 'info_core'})
print(table_total_test)
tds_total_test = table_total_test.find_all('span')
kr_total_test = tds_total_test[4].text.strip()
print(kr_total_test)
print()

#전일대비 사망자 증가수
table_d = soup2.find('div', {'class': 'liveNum'})
#print(table_d)
data_d = table_d.find_all('span', {'class': 'before'})
#print(data_d)
prev_death = data_d[3].text.strip()
#print(prev_death)
prev_death = prev_death.replace("(","")
prev_death = prev_death.replace("+","")
prev_death = prev_death.replace(" ","")
prev_death = prev_death.replace(")","")
#print(prev_death)

#전세계 확진자수

