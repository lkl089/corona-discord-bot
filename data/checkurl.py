# -*- coding:utf-8 -*-
import urllib.request
import urllib.error
from datetime import datetime,date,timedelta
from selenium import webdriver


#driver = webdriver.Chrome('c:/chromedriver/chromedriver.exe')
#driver.implicitly_wait(2)
#driver.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=')
#chart1 = driver.find_elements_by_xpath('//*[@id="content"]/div/div[5]/div[1]')
#print(chart1)
#driver.quit()

now = datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")
today = month + day

url1 = "http://ncov.mohw.go.kr/static/image/main_chart/live_pdata1_" + today + ".png"
url2 = "http://ncov.mohw.go.kr/static/image/main_chart/live_pdata2_" + today + ".png"
#url3 = ""
try:
    res = urllib.request.urlopen(url1)
    print(res.status)
    print("URL1 is alive")
    update = month+"/"+day+" 기준"
except urllib.error.HTTPError as e:
    err = e.read()
    code = e.getcode()
    broke = "URL1 is broken"
    print(code)  ## 404
    print(broke)
    today = date.today() - timedelta(1)
    month = today.strftime("%m")
    day = today.strftime("%d")
    today = month + day
    print(today)
    update = month + "/" + day + " 기준"

try:
    res = urllib.request.urlopen(url2)
    print(res.status)
    print("URL2 is alive")
    update = month + "/" + day + " 기준"
except urllib.error.HTTPError as e:
    err = e.read()
    code = e.getcode()
    broke="URL2 is broken"
    print(code)  ## 404
    print(broke)
    today = date.today() - timedelta(1)
    month = today.strftime("%m")
    day = today.strftime("%d")
    today = month + day
    print(today)
    update = month + "/" + day + " 기준"

#try:
#    res = urllib.request.urlopen(url3)
#    print(res.status)
#except urllib.error.HTTPError as e:
#    err = e.read()
#    code = e.getcode()
#    print(code+"URL1 is broken")  ## 404