from bs4 import BeautifulSoup
from urllib.request import Request
import urllib.error


url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=14&ncvContSeq=&contSeq=&board_id=&gubun="
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

table = soup.find('table', {'class': 'num minisize'})
#print(table)
ths = table.find_all('th')
list_country = []
for count in range(9, 28):
    list_country.append([ths[count]])
print(list_country)
tds = table.find_all('td')
#print('=======')
#print(ths)
#print('=======')
#print(tds)
#print('=======')

# 6일전 ~ 오늘
day6 = ths[1].text.strip()
day5 = ths[2].text.strip()
day4 = ths[3].text.strip()
day3 = ths[4].text.strip()
day2 = ths[5].text.strip()
day1 = ths[6].text.strip()
today = ths[7].text.strip()

print(day6)
print(day5)
print(day4)
print(day3)
print(day2)
print(day1)
print(today)


no1 = list_country[0][0].text.strip()
w_1_6 = tds[0].text.strip()
w_1_6 = w_1_6.replace("명","")
w_1_5 = tds[1].text.strip()
w_1_5 = w_1_5.replace("명","")
w_1_4 = tds[2].text.strip()
w_1_4 = w_1_4.replace("명","")
w_1_3 = tds[3].text.strip()
w_1_3 = w_1_3.replace("명","")
w_1_2 = tds[4].text.strip()
w_1_2 = w_1_2.replace("명","")
w_1_1 = tds[5].text.strip()
w_1_1 = w_1_1.replace("명","")
w_1_1_p = w_1_1.replace(",","")
w_1_t = tds[6].text.strip()
w_1_t = w_1_t.replace("명","")
w_1_t_p = w_1_t.replace(",","")
w_1_d = tds[7].text.strip()
w_1_d = w_1_d.replace("명","")
w_1_d = w_1_d.replace("(","")
w_1_d = w_1_d.replace(")","")
print(no1)
print(w_1_6)
print(w_1_5)
print(w_1_4)
print(w_1_3)
print(w_1_2)
print(w_1_1)
print(w_1_t)
print(w_1_d)

print(int(w_1_t_p)-int(w_1_1_p))


# 2순위 감염국 ~ 19순위 감염국
i=0
while i<19:
    i=i+1
    if (i==1):
        no2 = list_country[i][0].text.strip()
        w_2_6 = tds[int(0)+(int(8)*int(i))].text.strip()
        w_2_6 = w_2_6.replace("명", "")
        w_2_5 = tds[int(1)+(int(8)*int(i))].text.strip()
        w_2_5 = w_2_5.replace("명", "")
        w_2_4 = tds[int(2)+(int(8)*int(i))].text.strip()
        w_2_4 = w_2_4.replace("명", "")
        w_2_3 = tds[int(3)+(int(8)*int(i))].text.strip()
        w_2_3 = w_2_3.replace("명", "")
        w_2_2 = tds[int(4)+(int(8)*int(i))].text.strip()
        w_2_2 = w_2_2.replace("명", "")
        w_2_1 = tds[int(5)+(int(8)*int(i))].text.strip()
        w_2_1 = w_2_1.replace("명", "")
        w_2_1_p = w_2_1.replace(",", "")
        w_2_t = tds[int(6)+(int(8)*int(i))].text.strip()
        w_2_t = w_2_t.replace("명", "")
        w_2_t_p = w_2_t.replace(",", "")
        w_2_d = tds[int(7)+(int(8)*int(i))].text.strip()
        w_2_d = w_2_d.replace("명", "")
        w_2_d = w_2_d.replace("(", "")
        w_2_d = w_2_d.replace(")", "")
        print(no2)
        print(w_2_6)
        print(w_2_5)
        print(w_2_4)
        print(w_2_3)
        print(w_2_2)
        print(w_2_1)
        print(w_2_t)
        print(w_2_d)
        continue
    elif(i==2):
        no3 = list_country[i][0].text.strip()
        w_3_6 = tds[int(0)+(int(8)*int(i))].text.strip()
        w_3_6 = w_3_6.replace("명", "")
        w_3_5 = tds[int(1)+(int(8)*int(i))].text.strip()
        w_3_5 = w_3_5.replace("명", "")
        w_3_4 = tds[int(2)+(int(8)*int(i))].text.strip()
        w_3_4 = w_3_4.replace("명", "")
        w_3_3 = tds[int(3)+(int(8)*int(i))].text.strip()
        w_3_3 = w_3_3.replace("명", "")
        w_3_2 = tds[int(4)+(int(8)*int(i))].text.strip()
        w_3_2 = w_3_2.replace("명", "")
        w_3_1 = tds[int(5)+(int(8)*int(i))].text.strip()
        w_3_1 = w_3_1.replace("명", "")
        w_3_t = tds[int(6)+(int(8)*int(i))].text.strip()
        w_3_t =w_3_t.replace("명", "")
        w_3_d = tds[int(7)+(int(8)*int(i))].text.strip()
        w_3_d = w_3_d.replace("명", "")
        w_3_d = w_3_d.replace("(", "")
        w_3_d = w_3_d.replace(")", "")
        print(no3)
        print(w_3_6)
        print(w_3_5)
        print(w_3_4)
        print(w_3_3)
        print(w_3_2)
        print(w_3_1)
        print(w_3_t)
        print(w_3_d)
        continue
    elif (i == 3):
        no4 = list_country[i][0].text.strip()
        w_4_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_4_6 = w_4_6.replace("명", "")
        w_4_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_4_5 = w_4_5.replace("명", "")
        w_4_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_4_4 = w_4_4.replace("명", "")
        w_4_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_4_3 = w_4_3.replace("명", "")
        w_4_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_4_2 = w_4_2.replace("명", "")
        w_4_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_4_1 = w_4_1.replace("명", "")
        w_4_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_4_t = w_4_t.replace("명", "")
        w_4_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_4_d = w_4_d.replace("명", "")
        w_4_d = w_4_d.replace("(", "")
        w_4_d = w_4_d.replace(")", "")
        print(no4)
        print(w_4_6)
        print(w_4_5)
        print(w_4_4)
        print(w_4_3)
        print(w_4_2)
        print(w_4_1)
        print(w_4_t)
        print(w_4_d)
        continue
    elif (i == 4):
        no5 = list_country[i][0].text.strip()
        w_5_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_5_6 = w_5_6.replace("명", "")
        w_5_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_5_5 = w_5_5.replace("명", "")
        w_5_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_5_4 = w_5_4.replace("명", "")
        w_5_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_5_3 = w_5_3.replace("명", "")
        w_5_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_5_2 = w_5_2.replace("명", "")
        w_5_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_5_1 = w_5_1.replace("명", "")
        w_5_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_5_t = w_5_t.replace("명", "")
        w_5_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_5_d = w_5_d.replace("명", "")
        w_5_d = w_5_d.replace("(", "")
        w_5_d = w_5_d.replace(")", "")
        print(no5)
        print(w_5_6)
        print(w_5_5)
        print(w_5_4)
        print(w_5_3)
        print(w_5_2)
        print(w_5_1)
        print(w_5_t)
        print(w_5_d)
        continue
    elif (i == 5):
        no6 = list_country[i][0].text.strip()
        w_6_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_6_6 = w_6_6.replace("명", "")
        w_6_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_6_5 = w_6_5.replace("명", "")
        w_6_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_6_4 = w_6_4.replace("명", "")
        w_6_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_6_3 = w_6_3.replace("명", "")
        w_6_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_6_2 = w_6_2.replace("명", "")
        w_6_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_6_1 = w_6_1.replace("명", "")
        w_6_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_6_t = w_6_t.replace("명", "")
        w_6_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_6_d = w_6_d.replace("명", "")
        w_6_d = w_6_d.replace("(", "")
        w_6_d = w_6_d.replace(")", "")
        print(no6)
        print(w_6_6)
        print(w_6_5)
        print(w_6_4)
        print(w_6_3)
        print(w_6_2)
        print(w_6_1)
        print(w_6_t)
        print(w_6_d)
        continue
    elif (i == 6):
        no7 = list_country[i][0].text.strip()
        w_7_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_7_6 = w_7_6.replace("명", "")
        w_7_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_7_5 = w_7_5.replace("명", "")
        w_7_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_7_4 = w_7_4.replace("명", "")
        w_7_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_7_3 = w_7_3.replace("명", "")
        w_7_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_7_2 = w_7_2.replace("명", "")
        w_7_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_7_1 = w_7_1.replace("명", "")
        w_7_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_7_t = w_7_t.replace("명", "")
        w_7_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_7_d = w_7_d.replace("명", "")
        w_7_d = w_7_d.replace("(", "")
        w_7_d = w_7_d.replace(")", "")
        print(no7)
        print(w_7_6)
        print(w_7_5)
        print(w_7_4)
        print(w_7_3)
        print(w_7_2)
        print(w_7_1)
        print(w_7_t)
        print(w_7_d)
        continue
    elif (i == 7):
        no8 = list_country[i][0].text.strip()
        w_8_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_8_6 = w_8_6.replace("명", "")
        w_8_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_8_5 = w_8_5.replace("명", "")
        w_8_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_8_4 = w_8_4.replace("명", "")
        w_8_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_8_3 = w_8_3.replace("명", "")
        w_8_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_8_2 = w_8_2.replace("명", "")
        w_8_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_8_1 = w_8_1.replace("명", "")
        w_8_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_8_t = w_8_t.replace("명", "")
        w_8_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_8_d = w_8_d.replace("명", "")
        w_8_d = w_8_d.replace("(", "")
        w_8_d = w_8_d.replace(")", "")
        print(no8)
        print(w_8_6)
        print(w_8_5)
        print(w_8_4)
        print(w_8_3)
        print(w_8_2)
        print(w_8_1)
        print(w_8_t)
        print(w_8_d)
        continue
    elif (i == 8):
        no9 = list_country[i][0].text.strip()
        w_9_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_9_6 = w_9_6.replace("명", "")
        w_9_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_9_5 = w_9_5.replace("명", "")
        w_9_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_9_4 = w_9_4.replace("명", "")
        w_9_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_9_3 = w_9_3.replace("명", "")
        w_9_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_9_2 = w_9_2.replace("명", "")
        w_9_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_9_1 = w_9_1.replace("명", "")
        w_9_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_9_t = w_9_t.replace("명", "")
        w_9_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_9_d = w_9_d.replace("명", "")
        w_9_d = w_9_d.replace("(", "")
        w_9_d = w_9_d.replace(")", "")
        print(no9)
        print(w_9_6)
        print(w_9_5)
        print(w_9_4)
        print(w_9_3)
        print(w_9_2)
        print(w_9_1)
        print(w_9_t)
        print(w_9_d)
        continue
    elif (i == 9):
        no10 = list_country[i][0].text.strip()
        w_10_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_10_6 = w_10_6.replace("명", "")
        w_10_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_10_5 = w_10_5.replace("명", "")
        w_10_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_10_4 = w_10_4.replace("명", "")
        w_10_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_10_3 = w_10_3.replace("명", "")
        w_10_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_10_2 = w_10_2.replace("명", "")
        w_10_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_10_1 = w_10_1.replace("명", "")
        w_10_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_10_t = w_10_t.replace("명", "")
        w_10_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_10_d = w_10_d.replace("명", "")
        w_10_d = w_10_d.replace("(", "")
        w_10_d = w_10_d.replace(")", "")
        print(no10)
        print(w_10_6)
        print(w_10_5)
        print(w_10_4)
        print(w_10_3)
        print(w_10_2)
        print(w_10_1)
        print(w_10_t)
        print(w_10_d)
        continue
    elif (i == 10):
        no11 = list_country[i][0].text.strip()
        w_11_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_11_6 = w_11_6.replace("명", "")
        w_11_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_11_5 = w_11_5.replace("명", "")
        w_11_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_11_4 = w_11_4.replace("명", "")
        w_11_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_11_3 = w_11_3.replace("명", "")
        w_11_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_11_2 = w_11_2.replace("명", "")
        w_11_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_11_1 = w_11_1.replace("명", "")
        w_11_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_11_t = w_11_t.replace("명", "")
        w_11_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_11_d = w_11_d.replace("명", "")
        w_11_d = w_11_d.replace("(", "")
        w_11_d = w_11_d.replace(")", "")
        print(no11)
        print(w_11_6)
        print(w_11_5)
        print(w_11_4)
        print(w_11_3)
        print(w_11_2)
        print(w_11_1)
        print(w_11_t)
        print(w_11_d)
        continue
    elif (i == 11):
        no12 = list_country[i][0].text.strip()
        w_12_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_12_6 = w_12_6.replace("명", "")
        w_12_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_12_5 = w_12_5.replace("명", "")
        w_12_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_12_4 = w_12_4.replace("명", "")
        w_12_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_12_3 = w_12_3.replace("명", "")
        w_12_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_12_2 = w_12_2.replace("명", "")
        w_12_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_12_1 = w_12_1.replace("명", "")
        w_12_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_12_t = w_12_t.replace("명", "")
        w_12_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_12_d = w_12_d.replace("명", "")
        w_12_d = w_12_d.replace("(", "")
        w_12_d = w_12_d.replace(")", "")
        print(no12)
        print(w_12_6)
        print(w_12_5)
        print(w_12_4)
        print(w_12_3)
        print(w_12_2)
        print(w_12_1)
        print(w_12_t)
        print(w_12_d)
        continue
    elif (i == 12):
        no13 = list_country[i][0].text.strip()
        w_13_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_13_6 = w_13_6.replace("명", "")
        w_13_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_13_5 = w_13_5.replace("명", "")
        w_13_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_13_4 = w_13_4.replace("명", "")
        w_13_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_13_3 = w_13_3.replace("명", "")
        w_13_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_13_2 = w_13_2.replace("명", "")
        w_13_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_13_1 = w_13_1.replace("명", "")
        w_13_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_13_t = w_13_t.replace("명", "")
        w_13_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_13_d = w_13_d.replace("명", "")
        w_13_d = w_13_d.replace("(", "")
        w_13_d = w_13_d.replace(")", "")
        print(no13)
        print(w_13_6)
        print(w_13_5)
        print(w_13_4)
        print(w_13_3)
        print(w_13_2)
        print(w_13_1)
        print(w_13_t)
        print(w_13_d)
        continue
    elif (i == 13):
        no14 = list_country[i][0].text.strip()
        w_14_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_14_6 = w_14_6.replace("명", "")
        w_14_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_14_5 = w_14_5.replace("명", "")
        w_14_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_14_4 = w_14_4.replace("명", "")
        w_14_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_14_3 = w_14_3.replace("명", "")
        w_14_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_14_2 = w_14_2.replace("명", "")
        w_14_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_14_1 = w_14_1.replace("명", "")
        w_14_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_14_t = w_14_t.replace("명", "")
        w_14_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_14_d = w_14_d.replace("명", "")
        w_14_d = w_14_d.replace("(", "")
        w_14_d = w_14_d.replace(")", "")
        print(no14)
        print(w_14_6)
        print(w_14_5)
        print(w_14_4)
        print(w_14_3)
        print(w_14_2)
        print(w_14_1)
        print(w_14_t)
        print(w_14_d)
        continue
    elif (i == 14):
        no15 = list_country[i][0].text.strip()
        w_15_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_15_6 = w_15_6.replace("명", "")
        w_15_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_15_5 = w_15_5.replace("명", "")
        w_15_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_15_4 = w_15_4.replace("명", "")
        w_15_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_15_3 = w_15_3.replace("명", "")
        w_15_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_15_2 = w_15_2.replace("명", "")
        w_15_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_15_1 = w_15_1.replace("명", "")
        w_15_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_15_t = w_15_t.replace("명", "")
        w_15_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_15_d = w_15_d.replace("명", "")
        w_15_d = w_15_d.replace("(", "")
        w_15_d = w_15_d.replace(")", "")
        print(no15)
        print(w_15_6)
        print(w_15_5)
        print(w_15_4)
        print(w_15_3)
        print(w_15_2)
        print(w_15_1)
        print(w_15_t)
        print(w_15_d)
        continue
    elif (i == 15):
        no16 = list_country[i][0].text.strip()
        w_16_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_16_6 = w_16_6.replace("명", "")
        w_16_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_16_5 = w_16_5.replace("명", "")
        w_16_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_16_4 = w_16_4.replace("명", "")
        w_16_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_16_3 = w_16_3.replace("명", "")
        w_16_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_16_2 = w_16_2.replace("명", "")
        w_16_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_16_1 = w_16_1.replace("명", "")
        w_16_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_16_t = w_16_t.replace("명", "")
        w_16_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_16_d = w_16_d.replace("명", "")
        w_16_d = w_16_d.replace("(", "")
        w_16_d = w_16_d.replace(")", "")
        print(no16)
        print(w_16_6)
        print(w_16_5)
        print(w_16_4)
        print(w_16_3)
        print(w_16_2)
        print(w_16_1)
        print(w_16_t)
        print(w_16_d)
        continue
    elif (i == 16):
        no17 = list_country[i][0].text.strip()
        w_17_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_17_6 = w_17_6.replace("명", "")
        w_17_6 = w_17_6.replace(",", "")
        w_17_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_17_5 = w_17_5.replace("명", "")
        w_17_5 = w_17_5.replace(",", "")
        w_17_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_17_4 = w_17_4.replace("명", "")
        w_17_4 = w_17_4.replace(",", "")
        w_17_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_17_3 = w_17_3.replace("명", "")
        w_17_3 = w_17_3.replace(",", "")
        w_17_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_17_2 = w_17_2.replace("명", "")
        w_17_2 = w_17_2.replace(",", "")
        w_17_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_17_1 = w_17_1.replace("명", "")
        w_17_1 = w_17_1.replace(",", "")
        w_17_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_17_t = w_17_t.replace("명", "")
        w_17_t = w_17_t.replace(",", "")
        w_17_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_17_d = w_17_d.replace("명", "")
        w_17_d = w_17_d.replace("(", "")
        w_17_d = w_17_d.replace(")", "")
        print(no17)
        print(w_17_6)
        print(w_17_5)
        print(w_17_4)
        print(w_17_3)
        print(w_17_2)
        print(w_17_1)
        print(w_17_t)
        print(w_17_d)
        continue
    elif (i == 17):
        no18 = list_country[i][0].text.strip()
        w_18_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_18_6 = w_18_6.replace("명", "")
        w_18_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_18_5 = w_18_5.replace("명", "")
        w_18_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_18_4 = w_18_4.replace("명", "")
        w_18_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_18_3 = w_18_3.replace("명", "")
        w_18_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_18_2 = w_18_2.replace("명", "")
        w_18_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_18_1 = w_18_1.replace("명", "")
        w_18_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_18_t = w_18_t.replace("명", "")
        w_18_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_18_d = w_18_d.replace("명", "")
        w_18_d = w_18_d.replace("(", "")
        w_18_d = w_18_d.replace(")", "")
        print(no18)
        print(w_18_6)
        print(w_18_5)
        print(w_18_4)
        print(w_18_3)
        print(w_18_2)
        print(w_18_1)
        print(w_18_t)
        print(w_18_d)
        continue
    elif (i == 18):
        no19 = list_country[i][0].text.strip()
        w_19_6 = tds[int(0) + (int(8) * int(i))].text.strip()
        w_19_6 = w_19_6.replace("명", "")
        w_19_5 = tds[int(1) + (int(8) * int(i))].text.strip()
        w_19_5 = w_19_5.replace("명", "")
        w_19_4 = tds[int(2) + (int(8) * int(i))].text.strip()
        w_19_4 = w_19_4.replace("명", "")
        w_19_3 = tds[int(3) + (int(8) * int(i))].text.strip()
        w_19_3 = w_19_3.replace("명", "")
        w_19_2 = tds[int(4) + (int(8) * int(i))].text.strip()
        w_19_2 = w_19_2.replace("명", "")
        w_19_1 = tds[int(5) + (int(8) * int(i))].text.strip()
        w_19_1 = w_19_1.replace("명", "")
        w_19_t = tds[int(6) + (int(8) * int(i))].text.strip()
        w_19_t = w_19_t.replace("명", "")
        w_19_d = tds[int(7) + (int(8) * int(i))].text.strip()
        w_19_d = w_19_d.replace("명", "")
        w_19_d = w_19_d.replace("(", "")
        w_19_d = w_19_d.replace(")", "")
        print(no19)
        print(w_19_6)
        print(w_19_5)
        print(w_19_4)
        print(w_19_3)
        print(w_19_2)
        print(w_19_1)
        print(w_19_t)
        print(w_19_d)

# end
