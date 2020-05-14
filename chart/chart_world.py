from data import recent_confirmed as week
from matplotlib import pyplot as plt
from matplotlib import rc
import matplotlib.font_manager as fm
import platform
from datetime import datetime

#plt.plot([week.w_19_6,week.w_19_5,week.w_19_4,week.w_19_3,week.w_19_2,week.w_19_1,week.w_19_t],'--')
#plt.plot([week.w_18_6,week.w_18_5,week.w_18_4,week.w_18_3,week.w_18_2,week.w_18_1,week.w_18_t],'--')
#plt.plot([week.w_17_6,week.w_17_5,week.w_17_4,week.w_17_3,week.w_17_2,week.w_17_1,week.w_17_t],'--')
#plt.plot([week.w_16_6,week.w_16_5,week.w_16_4,week.w_16_3,week.w_16_2,week.w_16_1,week.w_16_t],'--')
#plt.plot([week.w_15_6,week.w_15_5,week.w_15_4,week.w_15_3,week.w_15_2,week.w_15_1,week.w_15_t],'--')
#plt.plot([week.w_14_6,week.w_14_5,week.w_14_4,week.w_14_3,week.w_14_2,week.w_14_1,week.w_14_t],'--')
#plt.plot([week.w_13_6,week.w_13_5,week.w_13_4,week.w_13_3,week.w_13_2,week.w_13_1,week.w_13_t],'--')
#plt.plot([week.w_12_6,week.w_12_5,week.w_12_4,week.w_12_3,week.w_12_2,week.w_12_1,week.w_12_t],'--')
#plt.plot([week.w_11_6,week.w_11_5,week.w_11_4,week.w_11_3,week.w_11_2,week.w_11_1,week.w_11_t],'--')
#plt.plot([week.w_10_6,week.w_10_5,week.w_10_4,week.w_10_3,week.w_10_2,week.w_10_1,week.w_10_t],'--')
#plt.plot([week.w_9_6,week.w_9_5,week.w_9_4,week.w_9_3,week.w_9_2,week.w_9_1,week.w_9_t],'--')
#plt.plot([week.w_8_6,week.w_8_5,week.w_8_4,week.w_8_3,week.w_8_2,week.w_8_1,week.w_8_t],'--')
#plt.plot([week.w_7_6,week.w_7_5,week.w_7_4,week.w_7_3,week.w_7_2,week.w_7_1,week.w_7_t],'--')
#plt.plot([week.w_6_6,week.w_6_5,week.w_6_4,week.w_6_3,week.w_6_2,week.w_6_1,week.w_6_t],'--')
#plt.plot([week.w_5_6,week.w_5_5,week.w_5_4,week.w_5_3,week.w_5_2,week.w_5_1,week.w_5_t],'--')
#plt.plot([week.w_4_6,week.w_4_5,week.w_4_4,week.w_4_3,week.w_4_2,week.w_4_1,week.w_4_t],'--')
#plt.plot([week.w_3_6,week.w_3_5,week.w_3_4,week.w_3_3,week.w_3_2,week.w_3_1,week.w_3_t],'--')
#plt.plot([week.w_2_6,week.w_2_5,week.w_2_4,week.w_2_3,week.w_2_2,week.w_2_1,week.w_2_t],'--')
#plt.plot([week.w_1_6,week.w_1_5,week.w_1_4,week.w_1_3,week.w_1_2,week.w_1_1,week.w_1_t],'--')
#ago = ['6days ago','6days ago','6days ago','6days ago','6days ago','6days ago','today']
#x = range(len(ago))
#font_name = fm.FontProperties(fname="C:/Windows/Fonts/NanumBarunGothic.ttf").get_name()
#rc('font', family=font_name)

now = datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")
today = month + day

if platform.system() == 'Windows':
# 윈도우인 경우
    font_name = fm.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:
# 우분투인 경우
    font_name = fm.FontProperties(fname="/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf").get_name()
    rc('font', family=font_name)

ax = plt.subplot()
plt.title(month+"/"+day+'  주요 발생국가 상황')
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
plt.xticks(fontsize=8)
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
ax.set_xticklabels(['',week.no19, week.no18, week.no17, week.no16, week.no15, week.no14, week.no13, week.no12, week.no11, week.no10, week.no9, week.no8, week.no7, week.no6, week.no5, week.no4, week.no3 ,week.no2 ,week.no1], rotation=40)

confimed = ['0',week.w_19_t, week.w_18_t, week.w_17_t, week.w_16_t, week.w_15_t,week.w_14_t,week.w_13_t,week.w_12_t,week.w_11_t,week.w_10_t,week.w_9_t,week.w_8_t,week.w_7_t,week.w_6_t,week.w_5_t,week.w_4_t,week.w_3_t,week.w_2_t,week.w_1_t]
dead = [week.w_19_d, week.w_18_d, week.w_17_d, week.w_16_d, week.w_15_d,week.w_14_d,week.w_13_d,week.w_12_d,week.w_11_d,week.w_10_d,week.w_9_d,week.w_8_d,week.w_7_d,week.w_6_d,week.w_5_d,week.w_4_d,week.w_3_d,week.w_2_d,week.w_1_d]
print(confimed)
print(dead)
plt.bar(range(len(confimed)), confimed)

plt.legend(['확진자'])

#plt.xlabel('국가')                  # x축 라벨
#plt.ylabel('확진자')                  # y축 라벨
plt.draw()
fig = plt.gcf()

if platform.system() == 'Windows':
# 윈도우인 경우
    world_chart = fig.savefig('data/confim_nara.png', dpi=fig.dpi)
else:
# 우분투인 경우
    world_chart = fig.savefig('/discord-bot/data/confim_nara.png', dpi=fig.dpi)


#plt.show()
plt.cla()
plt.clf()

