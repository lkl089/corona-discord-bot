from bs4 import BeautifulSoup
from urllib.request import Request
import urllib.error
from data import data
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
w_confirmed = w_tds[2].text.strip()
print(w_confirmed)

#전일대비 증가
w_prev_confirmed = w_tds[3].text.strip()
w_prev_confirmed = w_prev_confirmed.replace("+","")
print(w_prev_confirmed)

#전세계 사망자
w_death = w_tds[4].text.strip()
print(w_death)

#전일대비 증가
w_prev_death = w_tds[5].text.strip()
w_prev_death = w_prev_death.replace("+","")
print(w_prev_death)

#전세계 완치자
w_rescued = w_tds[6].text.strip()
print(w_rescued)

#전세계 치료중인자
w_active = w_tds[8].text.strip()
print(w_active)
print("world end")
print("=======")
i=0
ths = w_soup.find_all('tr')
all_country = []
for count in range(9, 456): #232 china 시작 ~ 446 saint pierre miquelon 까지 215개 국가
    #if count == :
        #
    #else :
        #
    all_country.append([ths[count]])
    print('==='+str(i)+'번 ===')
    print(all_country[i][0].text.strip())
    i = i + 1


#미국
usa = w_soup.find_all('tr')
usa_all = usa[9]
usa_all = usa_all.find_all('td')
usa_confim = usa_all[2].text.strip()
usa_confim_rd = usa_confim.replace(",","")
usa_prev_confim = usa_all[3].text.strip()
usa_prev_confim = usa_prev_confim.replace("+","")
usa_dead = usa_all[4].text.strip()
usa_prev_dead = usa_all[5].text.strip()
usa_prev_dead = usa_prev_dead.replace("+","")
usa_rescued = usa_all[6].text.strip()
usa_active = usa_all[8].text.strip()
usa_total_test = usa_all[12].text.strip()
usa_confim_percent = ''
if usa_total_test == 'N/A':
    usa_confim_percent = 'N/A (정보없음)'
else:
    usa_total_test_rd = usa_total_test.replace(",", "")
    usa_confim_percent = str(round(float(int(usa_confim_rd) / int(usa_total_test_rd) * int(100)), 2))


print(usa)
print('here!!!')
print(len(usa))
print(usa_all)
print('==11==')
print(usa_confim)
print(usa_prev_confim)
print(usa_dead)
print(usa_prev_dead)
print(usa_rescued)
print(usa_active)
#print(usa_confim)

##영국
print("this England")
UK_all = all_country[4][0]
UK = UK_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(UK_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
UK_confim = UK[2].text.strip()
UK_confim_rd = UK_confim.replace(",","")
print(UK_confim)
UK_prev_confim = UK[3].text.strip()
UK_prev_confim = UK_prev_confim.replace("+","")
print(UK_prev_confim)
UK_dead = UK[4].text.strip()
print(UK_dead)
UK_prev_dead = UK[5].text.strip()
UK_prev_dead = UK_prev_dead.replace("+","")
print(UK_prev_dead)
UK_rescued = UK[6].text.strip()
print(UK_rescued)
UK_active = UK[8].text.strip()
print(UK_active)
print(UK[12].text.strip())
UK_total_test = UK[12].text.strip()
print(UK_total_test)
print("확인")
UK_confim_percent = ''
if UK[12].text.strip() == 'N/A':
    UK_confim_percent = 'N/A (정보없음)'
elif UK[12].text.strip() == '':
    UK_confim_percent = 'N/A (정보없음)'
else:
    UK_total_test_rd = UK_total_test.replace(",", "")
    UK_confim_percent = str(round(float(int(UK_confim_rd) / int(UK_total_test_rd) * int(100)), 2))

##스페인
print(all_country[3][0])
print("this spain")

spain_all = all_country[3][0]
spain = spain_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(UK_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
spain_confim = spain[2].text.strip()
spain_confim_rd = spain_confim.replace(",","")
print(spain_confim)
spain_prev_confim = spain[3].text.strip()
spain_prev_confim = spain_prev_confim.replace("+","")
print(spain_prev_confim)
spain_dead = spain[4].text.strip()
print(spain_dead)
spain_prev_dead = spain[5].text.strip()
spain_prev_dead = spain_prev_dead.replace("+","")
print(spain_prev_dead)
spain_rescued = spain[6].text.strip()
print(spain_rescued)
spain_active = spain[8].text.strip()
print(spain_active)
spain_total_test = spain[12].text.strip()
spain_confim_percent = ''
if spain[12].text.strip() == 'N/A':
    spain_confim_percent = 'N/A (정보없음)'
elif spain[12].text.strip() == '':
    spain_confim_percent = 'N/A (정보없음)'
else:
    spain_total_test_rd = spain_total_test.replace(",", "")
    spain_confim_percent = str(round(float(int(spain_confim_rd) / int(spain_total_test_rd) * int(100)), 2))


##이탈리아
print(all_country[5][0])
print("this italy")

italy_all = all_country[5][0]
italy = italy_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(italy_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
italy_confim = italy[2].text.strip()
italy_confim_rd = italy_confim.replace(",","")
print(italy_confim)
italy_prev_confim = italy[3].text.strip()
italy_prev_confim = italy_prev_confim.replace("+","")
print(italy_prev_confim)
italy_dead = italy[4].text.strip()
print(italy_dead)
italy_prev_dead = italy[5].text.strip()
italy_prev_dead = italy_prev_dead.replace("+","")
print(italy_prev_dead)
italy_rescued = italy[6].text.strip()
print(italy_rescued)
italy_active = italy[8].text.strip()
print(italy_active)
italy_total_test = italy[12].text.strip()
italy_confim_percent = ''
if italy[12].text.strip() == 'N/A':
    italy_confim_percent = 'N/A (정보없음)'
elif italy[12].text.strip() == '':
    italy_confim_percent = 'N/A (정보없음)'
else:
    italy_total_test_rd = italy_total_test.replace(",", "")
    italy_confim_percent = str(round(float(int(italy_confim_rd) / int(italy_total_test_rd) * int(100)), 2))


##독일
print(all_country[240][0])
print("this germany")

germany_all = all_country[240][0]
germany = germany_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(germany_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
germany_confim = germany[2].text.strip()
germany_confim_rd = germany_confim.replace(",","")
print(germany_confim)
germany_prev_confim = germany[3].text.strip()
germany_prev_confim = germany_prev_confim.replace("+","")
print(germany_prev_confim)
germany_dead = germany[4].text.strip()
print(germany_dead)
germany_prev_dead = germany[5].text.strip()
germany_prev_dead = germany_prev_dead.replace("+","")
print(germany_prev_dead)
germany_rescued = germany[6].text.strip()
print(germany_rescued)
germany_active = germany[8].text.strip()
print(germany_active)
germany_total_test = germany[12].text.strip()
germany_confim_percent = ''
if germany[12].text.strip() == 'N/A':
    germany_confim_percent = 'N/A (정보없음)'
elif germany[12].text.strip() == '':
    germany_confim_percent = 'N/A (정보없음)'
else:
    germany_total_test_rd = germany_total_test.replace(",", "")
    germany_confim_percent = str(round(float(int(germany_confim_rd) / int(germany_total_test_rd) * int(100)), 2))


##터키
print(all_country[9][0])
print("this turkey")

turkey_all = all_country[9][0]
turkey = turkey_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(turkey_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
turkey_confim = turkey[2].text.strip()
turkey_confim_rd = turkey_confim.replace(",","")
print(turkey_confim)
turkey_prev_confim = turkey[3].text.strip()
turkey_prev_confim = turkey_prev_confim.replace("+","")
print(turkey_prev_confim)
turkey_dead = turkey[4].text.strip()
print(turkey_dead)
turkey_prev_dead = turkey[5].text.strip()
turkey_prev_dead = turkey_prev_dead.replace("+","")
print(turkey_prev_dead)
turkey_rescued = turkey[6].text.strip()
print(turkey_rescued)
turkey_active = turkey[8].text.strip()
print(turkey_active)
turkey_total_test = turkey[12].text.strip()
print(turkey_total_test)
turkey_confim_percent = ''
if turkey[12].text.strip() == 'N/A':
    turkey_confim_percent = 'N/A (정보없음)'
elif turkey[12].text.strip() == '':
    turkey_confim_percent = 'N/A (정보없음)'
else:
    turkey_total_test_rd = turkey_total_test.replace(",", "")
    turkey_confim_percent = str(round(float(int(turkey_confim_rd) / int(turkey_total_test_rd) * int(100)), 2))



##프랑스
print(all_country[11][0])
print("this france")

france_all = all_country[11][0]
france = france_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(france_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
france_confim = france[2].text.strip()
france_confim_rd = france_confim.replace(",","")
print(france_confim)
france_prev_confim = france[3].text.strip()
france_prev_confim = france_prev_confim.replace("+","")
print(france_prev_confim)
france_dead = france[4].text.strip()
print(france_dead)
france_prev_dead = france[5].text.strip()
france_prev_dead = france_prev_dead.replace("+","")
print(france_prev_dead)
france_rescued = france[6].text.strip()
print(france_rescued)
france_active = france[8].text.strip()
print(france_active)
france_total_test = france[12].text.strip()
france_confim_percent = ''
if france[12].text.strip() == 'N/A':
    france_confim_percent = 'N/A (정보없음)'
elif france[12].text.strip() == '':
    france_confim_percent = 'N/A (정보없음)'
else:
    france_total_test_rd = france_total_test.replace(",", "")
    france_confim_percent = str(round(float(int(france_confim_rd) / int(france_total_test_rd) * int(100)), 2))


##이란
print(all_country[10][0])
print("this iran")

iran_all = all_country[10][0]
iran = iran_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(iran_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
iran_confim = iran[2].text.strip()
iran_confim_rd = iran_confim.replace(",","")
print(iran_confim)
iran_prev_confim = iran[3].text.strip()
iran_prev_confim = iran_prev_confim.replace("+","")
print(iran_prev_confim)
iran_dead = iran[4].text.strip()
print(iran_dead)
iran_prev_dead = iran[5].text.strip()
iran_prev_dead = iran_prev_dead.replace("+","")
print(iran_prev_dead)
iran_rescued = iran[6].text.strip()
print(iran_rescued)
iran_active = iran[8].text.strip()
print(iran_active)
iran_total_test = iran[12].text.strip()
iran_confim_percent = ''
if iran[12].text.strip() == 'N/A':
    iran_confim_percent = 'N/A (정보없음)'
elif iran[12].text.strip() == '':
    iran_confim_percent = 'N/A (정보없음)'
else:
    iran_total_test_rd = france_total_test.replace(",", "")
    iran_confim_percent = str(round(float(int(iran_confim_rd) / int(iran_total_test_rd) * int(100)), 2))


##중국
print(all_country[214][0])
print("this china")

china_all = all_country[214][0]
china = china_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(china_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
china_confim = china[2].text.strip()
china_confim_rd = china_confim.replace(",","")
print(china_confim)
china_prev_confim = china[3].text.strip()
china_prev_confim = china_prev_confim.replace("+","")
print(china_prev_confim)
china_dead = china[4].text.strip()
print(china_dead)
china_prev_dead = china[5].text.strip()
china_prev_dead = china_prev_dead.replace("+","")
print(china_prev_dead)
china_rescued = china[6].text.strip()
print(china_rescued)
china_active = china[8].text.strip()
print(china_active)
china_total_test = china[12].text.strip()
china_confim_percent = ''
if china[12].text.strip() == 'N/A':
    china_confim_percent = 'N/A (정보없음)'
elif china[12].text.strip() == '':
    china_confim_percent = 'N/A (정보없음)'
else:
    china_total_test_rd = china_total_test.replace(",", "")
    china_confim_percent = str(round(float(int(china_confim_rd) / int(china_total_test_rd) * int(100)), 2))

##캐나다
print(all_country[10][0])
print("this canada")

canada_all = all_country[10][0]
canada = canada_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(canada_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
canada_confim = canada[2].text.strip()
canada_confim_rd = canada_confim.replace(",","")
print(canada_confim)
canada_prev_confim = canada[3].text.strip()
canada_prev_confim = canada_prev_confim.replace("+","")
print(canada_prev_confim)
canada_dead = canada[4].text.strip()
print(canada_dead)
canada_prev_dead = canada[5].text.strip()
canada_prev_dead = canada_prev_dead.replace("+","")
print(canada_prev_dead)
canada_rescued = canada[6].text.strip()
print(canada_rescued)
canada_active = canada[8].text.strip()
print(canada_active)
canada_total_test = canada[12].text.strip()
canada_confim_percent = ''
if canada[12].text.strip() == 'N/A':
    canada_confim_percent = 'N/A (정보없음)'
elif canada[12].text.strip() == '':
    canada_confim_percent = 'N/A (정보없음)'
else:
    canada_total_test_rd = canada_total_test.replace(",", "")
    canada_confim_percent = str(round(float(int(canada_confim_rd) / int(canada_total_test_rd) * int(100)), 2))

##벨기에
print(all_country[245][0])
print("this belgium")

belgium_all = all_country[245][0]
belgium = belgium_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(belgium_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
belgium_confim = belgium[2].text.strip()
belgium_confim_rd = belgium_confim.replace(",","")
print(belgium_confim)
belgium_prev_confim = belgium[3].text.strip()
belgium_prev_confim = belgium_prev_confim.replace("+","")
print(belgium_prev_confim)
belgium_dead = belgium[4].text.strip()
print(belgium_dead)
belgium_prev_dead = belgium[5].text.strip()
belgium_prev_dead = belgium_prev_dead.replace("+","")
print(belgium_prev_dead)
belgium_rescued = belgium[6].text.strip()
print(belgium_rescued)
belgium_active = belgium[8].text.strip()
print(belgium_active)
belgium_total_test = belgium[12].text.strip()
belgium_confim_percent = ''
if belgium[12].text.strip() == 'N/A':
    belgium_confim_percent = 'N/A (정보없음)'
elif belgium[12].text.strip() == '':
    belgium_confim_percent = 'N/A (정보없음)'
else:
    belgium_total_test_rd = belgium_total_test.replace(",", "")
    belgium_confim_percent = str(round(float(int(belgium_confim_rd) / int(belgium_total_test_rd) * int(100)), 2))


##네덜란드
print(all_country[252][0])
print("this nederlands")

nederlands_all = all_country[252][0]
nederlands = nederlands_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(nederlands_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
nederlands_confim = nederlands[2].text.strip()
nederlands_confim_rd = nederlands_confim.replace(",","")
print(nederlands_confim)
nederlands_prev_confim = nederlands[3].text.strip()
nederlands_prev_confim = nederlands_prev_confim.replace("+","")
print(nederlands_prev_confim)
nederlands_dead = nederlands[4].text.strip()
print(nederlands_dead)
nederlands_prev_dead = nederlands[5].text.strip()
nederlands_prev_dead = nederlands_prev_dead.replace("+","")
print(nederlands_prev_dead)
nederlands_rescued = nederlands[6].text.strip()
print(nederlands_rescued)
nederlands_active = nederlands[8].text.strip()
print(nederlands_active)
nederlands_total_test = nederlands[12].text.strip()
nederlands_confim_percent = ''
if nederlands[12].text.strip() == 'N/A':
    nederlands_confim_percent = 'N/A (정보없음)'
elif nederlands[12].text.strip() == '':
    nederlands_confim_percent = 'N/A (정보없음)'
else:
    nederlands_total_test_rd = nederlands_total_test.replace(",", "")
    nederlands_confim_percent = str(round(float(int(nederlands_confim_rd) / int(nederlands_total_test_rd) * int(100)), 2))



##스위스
print(all_country[27][0])
print("this swiss")

swiss_all = all_country[27][0]
swiss = swiss_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(swiss_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
swiss_confim = swiss[2].text.strip()
swiss_confim_rd = swiss_confim.replace(",","")
print(swiss_confim)
swiss_prev_confim = swiss[3].text.strip()
swiss_prev_confim = swiss_prev_confim.replace("+","")
print(swiss_prev_confim)
swiss_dead = swiss[4].text.strip()
print(swiss_dead)
swiss_prev_dead = swiss[5].text.strip()
swiss_prev_dead = swiss_prev_dead.replace("+","")
print(swiss_prev_dead)
swiss_rescued = swiss[6].text.strip()
print(swiss_rescued)
swiss_active = swiss[8].text.strip()
print(swiss_active)
swiss_total_test = swiss[12].text.strip()
swiss_confim_percent = ''
if swiss[12].text.strip() == 'N/A':
    swiss_confim_percent = 'N/A (정보없음)'
elif swiss[12].text.strip() == '':
    swiss_confim_percent = 'N/A (정보없음)'
else:
    swiss_total_test_rd = swiss_total_test.replace(",", "")
    swiss_confim_percent = str(round(float(int(swiss_confim_rd) / int(swiss_total_test_rd) * int(100)), 2))



##인도네시아
print(all_country[31][0])
print("this indonesia")

indonesia_all = all_country[31][0]
indonesia = indonesia_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(indonesia_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
indonesia_confim = indonesia[2].text.strip()
indonesia_confim_rd = indonesia_confim.replace(",","")
print(indonesia_confim)
indonesia_prev_confim = indonesia[3].text.strip()
indonesia_prev_confim = indonesia_prev_confim.replace("+","")
print(indonesia_prev_confim)
indonesia_dead = indonesia[4].text.strip()
print(indonesia_dead)
indonesia_prev_dead = indonesia[5].text.strip()
indonesia_prev_dead = indonesia_prev_dead.replace("+","")
print(indonesia_prev_dead)
indonesia_rescued = indonesia[6].text.strip()
print(indonesia_rescued)
indonesia_active = indonesia[8].text.strip()
print(indonesia_active)
indonesia_total_test = indonesia[12].text.strip()
indonesia_confim_percent = ''
if indonesia[12].text.strip() == 'N/A':
    indonesia_confim_percent = 'N/A (정보없음)'
elif indonesia[12].text.strip() == '':
    indonesia_confim_percent = 'N/A (정보없음)'
else:
    indonesia_total_test_rd = indonesia_total_test.replace(",", "")
    indonesia_confim_percent = str(round(float(int(indonesia_confim_rd) / int(indonesia_total_test_rd) * int(100)), 2))


##일본
print(all_country[271][0])
print("this japan")

japan_all = all_country[271][0]
japan = japan_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(japan_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
japan_confim = japan[2].text.strip()
japan_confim_rd = japan_confim.replace(",","")
print(japan_confim)
japan_prev_confim = japan[3].text.strip()
japan_prev_confim = japan_prev_confim.replace("+","")
print(japan_prev_confim)
japan_dead = japan[4].text.strip()
print(japan_dead)
japan_prev_dead = japan[5].text.strip()
japan_prev_dead = japan_prev_dead.replace("+","")
print(japan_prev_dead)
japan_rescued = japan[6].text.strip()
print(japan_rescued)
japan_active = japan[8].text.strip()
print(japan_active)
japan_total_test = japan[12].text.strip()
japan_confim_percent = ''
if japan[12].text.strip() == 'N/A':
    japan_confim_percent = 'N/A (정보없음)'
elif japan[12].text.strip() == '':
    japan_confim_percent = 'N/A (정보없음)'
else:
    japan_total_test_rd = japan_total_test.replace(",", "")
    japan_confim_percent = str(round(float(int(japan_confim_rd) / int(japan_total_test_rd) * int(100)), 2))


##필리핀
print(all_country[41][0])
print("this philippines")

philippines_all = all_country[41][0]
philippines = philippines_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(philippines_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
philippines_confim = philippines[2].text.strip()
philippines_confim_rd = philippines_confim.replace(",","")
print(philippines_confim)
philippines_prev_confim = philippines[3].text.strip()
philippines_prev_confim = philippines_prev_confim.replace("+","")
print(philippines_prev_confim)
philippines_dead = philippines[4].text.strip()
print(philippines_dead)
philippines_prev_dead = philippines[5].text.strip()
philippines_prev_dead = philippines_prev_dead.replace("+","")
print(philippines_prev_dead)
philippines_rescued = philippines[6].text.strip()
print(philippines_rescued)
philippines_active = philippines[8].text.strip()
print(philippines_active)
philippines_total_test = philippines[12].text.strip()
philippines_confim_percent = ''
if philippines[12].text.strip() == 'N/A':
    philippines_confim_percent = 'N/A (정보없음)'
elif philippines[12].text.strip() == '':
    philippines_confim_percent = 'N/A (정보없음)'
else:
    philippines_total_test_rd = philippines_total_test.replace(",", "")
    philippines_confim_percent = str(round(float(int(philippines_confim_rd) / int(philippines_total_test_rd) * int(100)), 2))



##태국
print(all_country[137][0])
print("this thailand")

thailand_all = all_country[245][0]
thailand =thailand_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(thailand_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
thailand_confim = thailand[2].text.strip()
thailand_confim_rd = thailand_confim.replace(",","")
print(thailand_confim)
thailand_prev_confim = thailand[3].text.strip()
thailand_prev_confim = thailand_prev_confim.replace("+","")
print(thailand_prev_confim)
thailand_dead = thailand[4].text.strip()
print(thailand_dead)
thailand_prev_dead = thailand[5].text.strip()
thailand_prev_dead = thailand_prev_dead.replace("+","")
print(thailand_prev_dead)
thailand_rescued = thailand[6].text.strip()
print(thailand_rescued)
thailand_active = thailand[8].text.strip()
print(thailand_active)
thailand_total_test = thailand[12].text.strip()
thailand_confim_percent = ''
if thailand[12].text.strip() == 'N/A':
    thailand_confim_percent = 'N/A (정보없음)'
elif thailand[12].text.strip() == '':
    thailand_confim_percent = 'N/A (정보없음)'
else:
    thailand_total_test_rd = thailand_total_test.replace(",", "")
    thailand_confim_percent = str(round(float(int(thailand_confim_rd) / int(thailand_total_test_rd) * int(100)), 2))



##베트남
print(all_country[145][0])
print("this vietnam")

vietnam_all = all_country[245][0]
vietnam = vietnam_all.find_all('td') # [0]=순서대로 카운트 [1]=국가명 [2]=확진자수 [3]= 전일대비확진자증가수 [4]=사망자수
print(vietnam_all)              # [5]=전일대비증가수 [6]=완치자수 [7]=격리자수 [8]=중증환자수 [9]=인구 백만명대비 검사수
                           # [10]=인구 백만명대비 사망자수 [11]=총검사수 [12]=인구 백만명 대비 검사수 [13]=인구수
vietnam_confim = vietnam[2].text.strip()
vietnam_confim_rd = vietnam_confim.replace(",","")
print(vietnam_confim)
vietnam_prev_confim = vietnam[3].text.strip()
vietnam_prev_confim = vietnam_prev_confim.replace("+","")
print(vietnam_prev_confim)
vietnam_dead = vietnam[4].text.strip()
print(vietnam_dead)
vietnam_prev_dead = vietnam[5].text.strip()
vietnam_prev_dead = vietnam_prev_dead.replace("+","")
print(vietnam_prev_dead)
vietnam_rescued = vietnam[6].text.strip()
print(vietnam_rescued)
vietnam_active = vietnam[8].text.strip()
print(vietnam_active)
vietnam_total_test = vietnam[12].text.strip()
vietnam_confim_percent = ''
if vietnam[12].text.strip() == 'N/A':
    vietnam_confim_percent = 'N/A (정보없음)'
elif vietnam[12].text.strip() == '':
    vietnam_confim_percent = 'N/A (정보없음)'
else:
    vietnam_total_test_rd = vietnam_total_test.replace(",", "")
    vietnam_confim_percent = str(round(float(int(vietnam_confim_rd) / int(vietnam_total_test_rd) * int(100)), 2))

confirm_percent = [usa_confim_percent,UK_confim_percent,spain_confim_percent,canada_confim_percent,belgium_confim_percent,china_confim_percent,france_confim_percent,germany_confim_percent,indonesia_confim_percent,iran_confim_percent,italy_confim_percent,japan_confim_percent,data.kr_confim_percent,nederlands_confim_percent,philippines_confim_percent,swiss_confim_percent,thailand_confim_percent,turkey_confim_percent,vietnam_confim_percent]
sorted(confirm_percent)
print(confirm_percent)

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
as_confirmed = as_tds[2].text.strip()
print(as_confirmed)

#전일대비 증가
as_prev_confirmed = as_tds[3].text.strip()
as_prev_confirmed = as_prev_confirmed.replace("+","")
print(as_prev_confirmed)

#아시아 사망자
as_death = as_tds[4].text.strip()
print(as_death)

#전일대비 증가
as_prev_death = as_tds[5].text.strip()
as_prev_death = as_prev_death.replace("+","")
print(as_prev_death)

#아시아 완치자
as_rescued = as_tds[6].text.strip()
print(as_rescued)

#아시아 치료중인자
as_active = as_tds[7].text.strip()
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
eu_confirmed = eu_tds[2].text.strip()
print(eu_confirmed)

#전일대비 증가
eu_prev_confirmed = eu_tds[3].text.strip()
eu_prev_confirmed = eu_prev_confirmed.replace("+","")
print(eu_prev_confirmed)

#유럽 사망자
eu_death = eu_tds[4].text.strip()
print(eu_death)

#전일대비 증가
eu_prev_death = eu_tds[5].text.strip()
eu_prev_death = eu_prev_death.replace("+","")
print(w_prev_death)

#유럽 완치자
eu_rescued = eu_tds[6].text.strip()
print(eu_rescued)

#유럽 치료중인자
eu_active = eu_tds[7].text.strip()
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
na_confirmed = na_tds[2].text.strip()
print(na_confirmed)

#전일대비 증가
na_prev_confirmed = na_tds[3].text.strip()
na_prev_confirmed = na_prev_confirmed.replace("+","")
print(na_prev_confirmed)

#북아메리카 사망자
na_death = na_tds[4].text.strip()
print(na_death)

#전일대비 증가
na_prev_death = na_tds[5].text.strip()
na_prev_death = na_prev_death.replace("+","")
print(na_prev_death)

#북아메리카 완치자
na_rescued = na_tds[6].text.strip()
print(na_rescued)

#북아메리카 치료중인자
na_active = na_tds[7].text.strip()
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
sa_confirmed = sa_tds[2].text.strip()
print(sa_confirmed)

#전일대비 증가
sa_prev_confirmed = sa_tds[3].text.strip()
sa_prev_confirmed = sa_prev_confirmed.replace("+","")
print(sa_prev_confirmed)

#남아메리카 사망자
sa_death = sa_tds[4].text.strip()
print(sa_death)

#전일대비 증가
sa_prev_death = sa_tds[5].text.strip()
sa_prev_death = sa_prev_death.replace("+","")
print(sa_prev_death)

#남아메리카 완치자
sa_rescued = sa_tds[6].text.strip()
print(sa_rescued)

#남아메리카 치료중인자
sa_active = sa_tds[7].text.strip()
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
af_confirmed = af_tds[2].text.strip()
print(af_confirmed)

#전일대비 증가
af_prev_confirmed = af_tds[3].text.strip()
af_prev_confirmed = af_prev_confirmed.replace("+","")
print(af_prev_confirmed)

#아프리카 사망자
af_death = af_tds[4].text.strip()
print(w_death)

#전일대비 증가
af_prev_death = af_tds[5].text.strip()
af_prev_death = af_prev_death.replace("+","")
print(w_prev_death)

#아프리카 완치자
af_rescued = af_tds[6].text.strip()
print(af_rescued)

#아프리카 치료중인자
af_active = af_tds[7].text.strip()
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
oc_confirmed = oc_tds[2].text.strip()
print(oc_confirmed)

#전일대비 증가
oc_prev_confirmed = oc_tds[3].text.strip()
oc_prev_confirmed = oc_prev_confirmed.replace("+","")
print(oc_prev_confirmed)

#오세아니아 사망자
oc_death = oc_tds[4].text.strip()
print(oc_death)

#전일대비 증가
oc_prev_death = oc_tds[5].text.strip()
oc_prev_death = oc_prev_death.replace("+","")
print(oc_prev_death)

#오세아니아 완치자
oc_rescued = oc_tds[6].text.strip()
print(w_rescued)

#오세아니아 치료중인자
oc_active = oc_tds[7].text.strip()
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
