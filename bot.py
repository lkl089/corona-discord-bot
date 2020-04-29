# -*- coding:utf-8 -*-
import discord, asyncio
from datetime import datetime
from data import data,checkurl,world_data,mask,token
from data.checkurl import update
from selenium import webdriver
from urllib.parse import quote
from urllib.request import Request, urlopen
import ssl
import json


client = discord.Client() # discord.Client() 같은 긴 단어 대신 client를 사용하겠다는 선언입니다.
token1 = token.token
print(token1)
prefix = "!" #접두어

now = datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")

ch = 0
for message in client.guilds:
    ch += len(message.channels)
@client.event

async def on_ready(): # 봇이 준비가 되면 1회 실행되는 부분입니다.
    print("봇 시작") # I'm Ready! 문구를 출력합니다.
    #
    await bt(['한국 확진자수 : '+data.confirmed+'명', '아시아 확진자수 : '+world_data.as_confirmed+'명',
              '유럽 확진자수 : '+world_data.eu_confirmed+'명','북미 확진자수 : '+world_data.na_confirmed+'명',
              '남미 확진자수 : '+world_data.sa_confirmed+'명','아프리카 확진자수 : '+world_data.af_confirmed+'명',
              '오세아니아 확진자수 : '+world_data.oc_confirmed+'명','만든사람 : KJH'])
    #print(client.user.name) # 봇의 이름을 출력합니다.
    #print(client.user.id) # 봇의 Discord 고유 ID를 출력합니다.

async def bt(zz):
#    await client.wait_until_ready()

    while not client.is_closed():
        for message in zz:
            await client.change_presence(status=discord.Status.online, activity=discord.Game(message))
            await asyncio.sleep(5) #5초마다 메세지 변경
            print(message)

@client.event
async def on_message(message, month=month, day=day, today=checkurl.today): # 메시지가 들어 올 때마다 가동되는 구문입니다.
    if message.author.bot: # 채팅을 친 사람이 봇일 경우
        return None # 반응하지 않고 구문을 종료합니다.

    if message.content == prefix+"명령어":

        embed = discord.Embed(title="명령어 목록",description="명령어 목록입니다.", color=0x62c1cc)
        embed.add_field(name="!한국", value="한국의 코로나 상황을 알려줍니다.",inline=False)
        embed.add_field(name="!현재상황", value="한국의 코로나 상황을 알려줍니다.",inline=False)
        embed.add_field(name="!격리해제", value="한국의 완치(격리해제) 상황을 알려줍니다.",inline=False)
        embed.add_field(name="!세계", value="전세계 코로나 확진자 정보를  알려줍니다.",inline=False)
        embed.add_field(name="!국가목록", value="[추가예정]각 국가명 입력시 해당 국가의 코로나 상황을 알려줍니다.", inline=False)
        embed.add_field(name="!아시아, !유럽, !북아메리카, !남아메리카, !아프리카, !오세아니아", value="각 대륙별 코로나 상황을 알려줍니다.", inline=False)
        #embed.add_field(name="!한국", value="한국의 코로나 상황을 알려줍니다.")
        await message.channel.send(embed=embed)
        # DM으로 메시지를 보냅니다.
        #await message.author.send("응답")

    if message.content == prefix+"마스크":
        mask_addr = message.content.split(maxsplit=1)
        print(mask_addr)
        embed = discord.Embed(title=month + "월 " + day + "일 "  + " 마스크 상황",description=mask.d[mask.y]+"요일 마스크 구매는 "+mask.buy_mask+"이 가능합니다\n"
                              +'현재 주변 '+str(mask.store_count)+'곳에서 판매중입니다.', color=0x9fd6f4)
   #     embed.add_field(name="누적 확진자수", value=data.confirmed + "명 :small_red_triangle:" + data.prev_confimed, inline=True)
        embed.set_image(url=mask.maps_url)
        embed.set_footer(text="현재 접속중인 ip를 기준으로 "+str(mask.dist)+"m 이내의 판매처를 검색합니다. \n현재 위치 오차는 약 "+str(mask.accu)+"m 입니다 ")
        await message.channel.send(embed=embed)
        print(message.author.id)

        u_id = message.author.id
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--lang=ko_KR")
        options.add_argument(
            'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

        driver = webdriver.Chrome('./data/chromedriver.exe', chrome_options=options)
        driver.get('https://discordresolver.c99.nl/index.php')
        driver.implicitly_wait(7)
        driver.find_element_by_xpath('/html/body/div/div[2]/div/form/input').send_keys(u_id)
        driver.find_element_by_xpath('/html/body/div/div[2]/div/form/button').click()
        driver.implicitly_wait(4)
        u_ip = driver.find_element_by_xpath('/html/body/div/div[3]/center/h1').text
        print(u_ip)

    if message.content == prefix+"현재상황":
        #기본적으로 한국의 정보를 가져옴
        country = "한국"
        embed = discord.Embed(title=month + "월 " + day + "일 " + country + " 코로나 상황", color=0x62c1cc)
        embed.add_field(name="누적 확진자수", value=data.confirmed + "명 :small_red_triangle:" + data.prev_confimed, inline=True)
        embed.add_field(name="격리해제", value=data.rescued + "명 :small_red_triangle:" + data.prev_rescured, inline=True)
        embed.add_field(name="격리중", value=data.cure + "명 :small_red_triangle:" + data.prev_confimed, inline=True)
        embed.add_field(name="사망자", value=data.dead + "명 :small_red_triangle:" + data.prev_death, inline=True)
        embed.set_image(url="http://ncov.mohw.go.kr/static/image/main_chart/live_pdata1_" + today + ".png")
        print(today)
        embed.set_footer(text=update)
        await message.channel.send(embed=embed)
    if message.content == prefix+"한국":

        print("요청")

        country="한국"
        embed = discord.Embed(title=month+"월 "+day+"일 "+country+" 코로나 상황", color=0x62c1cc)
        embed.add_field(name="누적 확진자수", value=data.confirmed+"명 :small_red_triangle:"+data.prev_confimed, inline=False)
        embed.add_field(name="격리해제", value=data.rescued + "명 :small_red_triangle:"+data.prev_rescured, inline=False)
        embed.add_field(name="격리중", value=data.cure + "명 :small_red_triangle:"+data.prev_confimed, inline=False)
        embed.add_field(name="사망자", value=data.dead + "명 :small_red_triangle:"+data.prev_death, inline=False)
        embed.set_image(url="http://ncov.mohw.go.kr/static/image/main_chart/live_pdata1_"+today+".png")
        print(today)
        embed.set_footer(text=update)
        await message.channel.send(embed=embed)
        #await message.channel.send("할 말", embed=embed)  # embed와 일반메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.

    if message.content == prefix+"격리해제":
        #기본적으로 한국의 정보를 가져옴
        embed = discord.Embed(title=month+"월 "+day+"일"+ " 코로나 상황", color=0x62c1cc)
        embed.add_field(name="누적 격리해제", value=data.rescued + "명 ", inline=True)
        embed.add_field(name="금일 격리해제", value=data.prev_rescured + "명 ", inline=True)
        embed.set_image(url="http://ncov.mohw.go.kr/static/image/main_chart/live_pdata2_" + today + ".png")
        embed.set_footer(text=update)
        await message.channel.send(embed=embed)

    if message.content == prefix+"세계":
        #전세계의 정보를 가져옴
        country = "전세계"
        embed = discord.Embed(title=month + "월 " + day + "일 " + country + " 코로나 상황", color=0xa83232)
        embed.add_field(name="누적 확진자수", value=world_data.w_confirmed + "명 :small_red_triangle:" + world_data.w_prev_confirmed, inline=False)
        embed.add_field(name="격리중", value=world_data.w_active + "명", inline=False)
        embed.add_field(name="격리해제", value=world_data.w_rescued + "명" , inline=False)
        embed.add_field(name="사망자", value=world_data.w_death + "명 :small_red_triangle:" + world_data.w_prev_death, inline=False)
        embed.set_image(url="http://ncov.mohw.go.kr/static/image/main_chart/live_pdata1_" + today + ".png")
        embed.set_footer(text=update)
        await message.channel.send(embed=embed)

    if message.content == prefix+"아시아":
        # 전세계의 정보를 가져옴
        country = "아시아"
        embed = discord.Embed(title=month + "월 " + day + "일 " + country + " 코로나 상황", color=0xa83232)
        embed.add_field(name="누적 확진자수",
                        value=world_data.as_confirmed + "명 :small_red_triangle:" + world_data.as_prev_confirmed,
                        inline=False)
        embed.add_field(name="격리중", value=world_data.as_active + "명", inline=False)
        embed.add_field(name="격리해제", value=world_data.as_rescued + "명", inline=False)
        embed.add_field(name="사망자", value=world_data.as_death + "명 :small_red_triangle:" + world_data.as_prev_death,
                        inline=False)
        embed.set_image(url="http://ncov.mohw.go.kr/static/image/main_chart/live_pdata1_" + today + ".png")
        embed.set_footer(text=update)
        await message.channel.send(embed=embed)

    if message.content == prefix+"유럽":
        # 전세계의 정보를 가져옴
        country = "유럽"
        embed = discord.Embed(title=month + "월 " + day + "일 " + country + " 코로나 상황", color=0xa83232)
        embed.add_field(name="누적 확진자수",
                        value=world_data.eu_confirmed + "명 :small_red_triangle:" + world_data.eu_prev_confirmed,
                        inline=False)
        embed.add_field(name="격리중", value=world_data.eu_active + "명", inline=False)
        embed.add_field(name="격리해제", value=world_data.eu_rescued + "명", inline=False)
        embed.add_field(name="사망자", value=world_data.eu_death + "명 :small_red_triangle:" + world_data.eu_prev_death,
                        inline=False)
        embed.set_image(url="http://ncov.mohw.go.kr/static/image/main_chart/live_pdata1_" + today + ".png")
        embed.set_footer(text=update)
        await message.channel.send(embed=embed)

    if message.content == prefix+"북아메리카":
        # 전세계의 정보를 가져옴
        country = "북아메리카"
        embed = discord.Embed(title=month + "월 " + day + "일 " + country + " 코로나 상황", color=0xa83232)
        embed.add_field(name="누적 확진자수",
                        value=world_data.na_confirmed + "명 :small_red_triangle:" + world_data.na_prev_confirmed,
                        inline=False)
        embed.add_field(name="격리중", value=world_data.na_active + "명", inline=False)
        embed.add_field(name="격리해제", value=world_data.na_rescued + "명", inline=False)
        embed.add_field(name="사망자", value=world_data.na_death + "명 :small_red_triangle:" + world_data.na_prev_death,
                        inline=False)
        embed.set_image(url="http://ncov.mohw.go.kr/static/image/main_chart/live_pdata1_" + today + ".png")
        embed.set_footer(text=update)
        await message.channel.send(embed=embed)

    if message.content == prefix+"남아메리카":
        # 전세계의 정보를 가져옴
        country = "남아메리카"
        embed = discord.Embed(title=month + "월 " + day + "일 " + country + " 코로나 상황", color=0xa83232)
        embed.add_field(name="누적 확진자수",
                        value=world_data.sa_confirmed + "명 :small_red_triangle:" + world_data.sa_prev_confirmed,
                        inline=False)
        embed.add_field(name="격리중", value=world_data.sa_active + "명", inline=False)
        embed.add_field(name="격리해제", value=world_data.sa_rescued + "명", inline=False)
        embed.add_field(name="사망자", value=world_data.sa_death + "명 :small_red_triangle:" + world_data.sa_prev_death,
                        inline=False)
        embed.set_image(url="http://ncov.mohw.go.kr/static/image/main_chart/live_pdata1_" + today + ".png")
        embed.set_footer(text=update)
        await message.channel.send(embed=embed)

    if message.content == prefix+"아프리카":
        # 전세계의 정보를 가져옴
        country = "아프리카"
        embed = discord.Embed(title=month + "월 " + day + "일 " + country + " 코로나 상황", color=0xa83232)
        embed.add_field(name="누적 확진자수",
                        value=world_data.af_confirmed + "명 :small_red_triangle:" + world_data.af_prev_confirmed,
                        inline=False)
        embed.add_field(name="격리중", value=world_data.af_active + "명", inline=False)
        embed.add_field(name="격리해제", value=world_data.af_rescued + "명", inline=False)
        embed.add_field(name="사망자", value=world_data.af_death + "명 :small_red_triangle:" + world_data.af_prev_death,
                        inline=False)
        embed.set_image(url="http://ncov.mohw.go.kr/static/image/main_chart/live_pdata1_" + today + ".png")
        embed.set_footer(text=update)
        await message.channel.send(embed=embed)

    if message.content == prefix+"오세아니아":
        # 전세계의 정보를 가져옴
        country = "오세아니아"
        embed = discord.Embed(title=month + "월 " + day + "일 " + country + " 코로나 상황", color=0xa83232)
        embed.add_field(name="누적 확진자수",
                        value=world_data.w_confirmed + "명 :small_red_triangle:" + world_data.w_prev_confirmed,
                        inline=False)
        embed.add_field(name="격리중", value=world_data.w_active + "명", inline=False)
        embed.add_field(name="격리해제", value=world_data.w_rescued + "명", inline=False)
        embed.add_field(name="사망자", value=world_data.w_death + "명 :small_red_triangle:" + world_data.w_prev_death,
                        inline=False)
        embed.set_image(url="http://ncov.mohw.go.kr/static/image/main_chart/live_pdata1_" + today + ".png")
        embed.set_footer(text=update)
        await message.channel.send(embed=embed)
    if message.content == prefix+"국가목록":

        embed = discord.Embed(title="명령어 목록",description="명령어 목록입니다.", color=0x62c1cc)
        embed.add_field(name="!한국", value="한국의 코로나 상황을 알려줍니다.",inline=False)
        embed.add_field(name="!현재상황", value="한국의 코로나 상황을 알려줍니다.",inline=False)
        embed.add_field(name="!격리해제", value="한국의 완치(격리해제) 상황을 알려줍니다.",inline=False)
        embed.add_field(name="!세계", value="전세계 코로나 확진자 정보를  알려줍니다.",inline=False)
        embed.add_field(name="!각나라별이름", value="[추가예정]각 나라별 코로나 상황을 알려줍니다.",inline=False)
        await message.channel.send(embed=embed)
client.run(token1) # 아까 넣어놓은 토큰 가져다가 봇을 실행하라는 부분입니다. 이 코드 없으면 구문이 아무리 완벽해도 실행되지 않습니다.
