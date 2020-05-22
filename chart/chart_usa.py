from data import recent_confirmed as week
from matplotlib import pyplot as plt
from matplotlib import rc
import matplotlib.font_manager as fm
import platform
from datetime import datetime

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
plt.title('주간 미국 코로나 상황 (보건복지부 자료기준)')
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
plt.xticks(fontsize=8)
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7])
ax.set_xticklabels(['',week.day6, week.day5, week.day4, week.day3, week.day2, week.day1, week.today], rotation=40)

confimed_usa = ['0',week.w_1_6, week.w_1_5, week.w_1_4, week.w_1_3, week.w_1_2,week.w_1_1,week.w_1_t]

print(confimed_usa)

plt.bar(range(len(confimed_usa)), confimed_usa)

plt.legend(['확진자'])

plt.draw()
fig = plt.gcf()
if platform.system() == 'Windows':
# 윈도우인 경우
    world_chart = fig.savefig('./data/confim_usa.png', dpi=fig.dpi)
else:
# 우분투인 경우
    world_chart = fig.savefig('/discord-bot/data/confim_usa.png', dpi=fig.dpi)


plt.cla()
plt.clf()