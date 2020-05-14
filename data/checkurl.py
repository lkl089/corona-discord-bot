# -*- coding:utf-8 -*-
import urllib.request
import urllib.error
from datetime import datetime,date,timedelta
from data import recent_confirmed as week


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


now = datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")
today = month + '.' + day
print('here!!')
print(today)
print(week.today)
if today == week.today:
    update = month+"/"+day+" 기준"
    print(update)
else:
    today = date.today() - timedelta(1)
    month = today.strftime("%m")
    day = today.strftime("%d")
    today = month + day
    update = month + "/" + day + " 기준"
    print(update)
