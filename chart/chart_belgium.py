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
plt.title('주간 벨기에 코로나 상황')
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
plt.xticks(fontsize=8)
ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7])
ax.set_xticklabels(['',week.day6, week.day5, week.day4, week.day3, week.day2, week.day1, week.today], rotation=40)

confimed_bel = ['0',week.w_11_6, week.w_11_5, week.w_11_4, week.w_11_3, week.w_11_2,week.w_11_1,week.w_11_t]

print(confimed_bel)

plt.bar(range(len(confimed_bel)), confimed_bel)

plt.legend(['확진자'])

plt.draw()
fig = plt.gcf()
if platform.system() == 'Windows':
# 윈도우인 경우
    world_chart = fig.savefig('./data/confim_belgium.png', dpi=fig.dpi)
else:
# 우분투인 경우
    world_chart = fig.savefig('/discord-bot/data/confim_belgium.png', dpi=fig.dpi)


plt.cla()
plt.clf()