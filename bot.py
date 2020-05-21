# -*- coding:utf-8 -*-
from data import recent_confirmed as week
import json
import os
import sys
import discord, asyncio
from datetime import datetime
from data import data,checkurl, world_data
from data.checkurl import update
import data.data as korea
from data import token
import requests
from urllib.parse import quote
import urllib.request
import platform
from chart import chart_world,chart_korea,chart_usa,chart_england


client_id = token.client_id
client_secret = token.client_secret

client = discord.Client()
token1 = token.token

prefix = "!"  # 접두어

now = datetime.now()
month = now.strftime("%m")
day = now.strftime("%d")

ch = 0
for message in client.guilds:
    ch += len(message.channels)


@client.event
async def on_ready():
    print("봇 시작")
    #
    await bt(['한국 확진자수 : ' + korea.confirmed + '명', '아시아 확진자수 : ' + world_data.as_confirmed + '명',
              '유럽 확진자수 : ' + world_data.eu_confirmed + '명', '북미 확진자수 : ' + world_data.na_confirmed + '명',
              '남미 확진자수 : ' + world_data.sa_confirmed + '명', '아프리카 확진자수 : ' + world_data.af_confirmed + '명',
              '오세아니아 확진자수 : ' + world_data.oc_confirmed + '명', '만든사람 : KJH'])
    # print(client.user.name) # 봇의 이름을 출력합니다.
    # print(client.user.id) # 봇의 Discord 고유 ID를 출력합니다.


async def bt(zz):
    #    await client.wait_until_ready()

    while not client.is_closed():
        for message in zz:
            await client.change_presence(status=discord.Status.online, activity=discord.Game(message))
            await asyncio.sleep(10)  # 5초마다 메세지 변경
            print(message)


@client.event
async def on_message(message, month=month, day=day, today=checkurl.today, maskinfo=[],
                     mark=[],stop=[],stop_c=[],stop_sell=''):  # 메시지가 들어 올 때마다 가동되는 구문입니다.
    if message.author.bot:  # 채팅을 친 사람이 봇일 경우
        return None  # 반응하지 않고 구문을 종료합니다.

    if message.content == prefix + "명령어":
        embed = discord.Embed(title="명령어 목록", description="명령어 목록입니다.", color=0x62c1cc)
        embed.add_field(name="!한국", value="한국의 코로나 상황을 알려줍니다.", inline=False)
        embed.add_field(name="!세계", value="전세계 코로나 확진자 정보를  알려줍니다.", inline=False)
        embed.add_field(name="!국가목록", value="[추가예정]각 국가명 입력시 해당 국가의 코로나 상황을 알려줍니다.", inline=False)
        embed.add_field(name="!아시아, !유럽, !북아메리카, !남아메리카, !아프리카, !오세아니아", value="각 대륙별 코로나 상황을 알려줍니다.", inline=False)
        # embed.add_field(name="!한국", value="한국의 코로나 상황을 알려줍니다.")
        await message.channel.send(embed=embed)
        # DM으로 메시지를 보냅니다.
        # await message.author.send("응답")
    if message.content == prefix + "목록":
        embed = discord.Embed(title="명령어 목록", description="명령어 목록입니다.", color=0x62c1cc)
        embed.add_field(name="!한국", value="한국의 코로나 상황을 알려줍니다.", inline=False)
        embed.add_field(name="!세계", value="전세계 코로나 확진자 정보를  알려줍니다.", inline=False)
        embed.add_field(name="!마스크 '주소'", value="입력한 주소지의 공적마스크 판매처를 검색합니다", inline=False)
        embed.add_field(name="!국가목록", value="[추가예정]각 국가명 입력시 해당 국가의 코로나 상황을 알려줍니다.", inline=False)
        embed.add_field(name="!아시아, !유럽, !북아메리카, !남아메리카, !아프리카, !오세아니아", value="각 대륙별 코로나 상황을 알려줍니다.", inline=False)
        # embed.add_field(name="!한국", value="한국의 코로나 상황을 알려줍니다.")
        #id = str(710687517275586580)
        #emoji = client.get_emoji(str(id))
        emoji = 'U+003AU+0066U+006CU+0061U+0067U+005FU+006BU+0072U+003A'
        await message.channel.send(embed=embed)
        await message.add_reaction(emoji)

        async def on_reaction_add(reaction, user):
            if reaction.emoji == ':flag_kr:':
                message.add_react(':flag_kr:')
                message.add_react(':globe_with_meridians:')



    if message.content.startswith(prefix + "마스크"):
        split_addr = message.content.split(maxsplit=1)
        len_addr = len(split_addr)
        print(len_addr)
        if len_addr == 1:
            embed = discord.Embed(title="공적 마스크 판매처 조회방법",
                                  description="'!마스크 서울특별시 양천구 신월동' 과 같이 주소를 입력해주세요\n" +
                                              "특별시,광역시의 경우 '시'라고만 적을경우 조회가 안될수 있습니다.\n" +
                                              "동의 경우 신월2동이면 신월동으로 입력함. (신주소 기반)\n" +
                                              "주소 입력 예시 >> 서울특별시 양천구 신월동 , 부산광역시 북구 구포동 ", color=0x9fd6f4)
            await message.channel.send(embed=embed)
        mask_addr = split_addr[1]
        # print(mask_addr)
        mask_api_addr = 'https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json?address=' + str(
            mask_addr)
        # print(mask_api_addr)
        API_KEY = token.API_KEY
        get_mask = requests.get(mask_api_addr)
        mask_all = get_mask.json()
        list(mask_all.keys())
        store_count = mask_all['count']
        mask_info = mask_all['stores']
        # print(mask_info)

        i = 1;

        for i in range(int(store_count) + 1):
            if i == store_count:
                print('mask info end')
                continue
            all_store = mask_info[i]
            all_addr = mask_info[i]
#           remain_mask = mask_info[i]
            stock = mask_info[i]
            lat = mask_info[i]
            lng = mask_info[i]

            location = str(lat['lat']) + ',' + str(lng['lng'])
            mark.append(location)
            # print(mark)
            if str(stock['remain_stat']) == 'plenty':
                remain = str(':green_circle:')
                stop.append(str(0))
            elif str(stock['remain_stat']) == 'some':
                remain = str(':orange_circle:')
                stop.append(str(0))
            elif str(stock['remain_stat']) == 'few':
                remain = str(':red_circle:')
                stop.append(str(0))
            elif str(stock['remain_stat']) == 'empty':
                remain = str(':black_circle:')
                stop.append(str(0))
            else:
                print(stock['remain_stat'])

                stop.append(str(int(i+1)))
                stop_c.append(i)
                print(stop)
                print(stop_c)
                cnt_stop = len(stop_c)
                stop_sell = stop.index(str(int(i+1)))
                print(stop_sell)
                remain = str(':x:')

            if str(stock['created_at']) == 'None':
                creat_at = str('정보 없음')
            else:
                creat_at = str(stock['created_at'])

            if str(stock['stock_at']) == 'None':
                stock_at = str('정보 없음')
            else:
                stock_at = str(stock['stock_at'])

            if i == stop_sell:
                print(stop)
                continue
            else:

                shops_map = 'https://maps.googleapis.com/maps/api/staticmap?center=' + str(location) + \
                        '&zoom=16&size=300x300&maptype=roadmap&region=kr&format=png' + '&markers=color:blue|label:' + str(
                    all_store['name']) + '|' + \
                        str(location) + '&key=' + API_KEY
                open_map = 'https://www.google.com/maps/search/' + str(location)
                info = str(int(i) + 1) + '. ' + '상점명 : ' + str(all_store['name']) + '\n주소 : ' + str(
                    all_addr['addr']) + '\n마스크 재고 : ' + remain + '\n입고시간 : ' + str(stock_at) + \
                        '\n갱신시간 : ' + str(creat_at) + '\n[길찾기](' + open_map + ')'
                maskinfo.append(info)
                # print(maskinfo)
                embed = discord.Embed(title="공적마스크 판매 상점 정보",
                                  description=info, color=0x9fd6f4)
                embed.set_footer(text='\n100개 이상(녹색),30개~99개(노랑색),2개~30개(빨강색),1개이하(검정색),판매중단(X)')
                embed.set_image(url=shops_map)
                await message.channel.send(embed=embed)
                # await message.channel.send(info)


        marker = []

        for i in range(int(store_count)):
            loop_m = '&markers=color:blue|' + str(mark[i])
            marker.append(loop_m)
            if i == store_count:
                continue
            # print(marker)
            # print(i)
        maps_url = 'https://maps.googleapis.com/maps/api/staticmap?zoom=14&size=600x600&maptype=roadmap&region=kr&format=png' + str(
            ''.join(marker)) + '&key=' + API_KEY
        print(maps_url)

        encText = urllib.parse.quote(maps_url)
        data = "url=" + encText
        url = "https://openapi.naver.com/v1/util/shorturl"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()  #
        res = json.load(response)
        list(res.keys())
        # response_body = res.read()#
        # if (rescode == 200):#
        #    response_body = response.read()#
        #    print(response_body.decode('utf-8'))#
        # else:#
        #   print("Error Code:" + rescode)#

        url_api = res['result']
        print(url_api)
        short_url = url_api['url']
        print(short_url)

        d = ['월', '화', '수', '목', '금', '토', '일']
        y = datetime.today().weekday()
        print(d[y])
        if y == 0:
            buy_mask = '주민번호 끝자리 1,6년생'
        elif y == 1:
            buy_mask = '주민번호 끝자리 2,7년생'
        elif y == 2:
            buy_mask = '주민번호 끝자리 3,8년생'
        elif y == 3:
            buy_mask = '주민번호 끝자리 4,9년생'
        elif y == 4:
            buy_mask = '주민번호 끝자리 5,0년생'
        elif y == 5:
            buy_mask = '모든사람'
        elif y == 6:
            buy_mask = '모든사람'

        embed = discord.Embed(title=month + "월 " + day + "일 " + " 마스크 상황",
                              description=d[y] + "요일 마스크 구매는 " + buy_mask + "이 가능합니다\n"
                                          + '판매 중지 '+str(cnt_stop)+'곳을 제외한 ' + str(int(store_count)-int(cnt_stop)) + '곳에서 구매 가능합니다.\n'
                                          + '전체목록 지도 : ' + short_url, color=0x9fd6f4)
        embed.set_footer(text="기준 주소 : " + str(mask_addr))
        await message.channel.send(embed=embed)

    if message.content == prefix + "한국":
        print("요청")

        country = "한국"
        embed = discord.Embed(title=month + "월 " + day + "일 " + country + " 코로나 상황", color=0x62c1cc)
        embed.add_field(name="누적 확진자수", value=korea.confirmed + "명 :small_red_triangle:" + korea.prev_confimed,
                        inline=False)
        embed.add_field(name="격리해제", value=korea.rescued + "명 :small_red_triangle:" + korea.prev_rescured, inline=False)
        embed.add_field(name="격리중", value=korea.cure + "명 :small_red_triangle:" + korea.prev_confimed, inline=False)
        embed.add_field(name="사망자", value=korea.dead + "명 :small_red_triangle:" + korea.prev_death, inline=False)
        embed.set_image(url="http://ncov.mohw.go.kr/static/image/main_chart/live_pdata1_" + today + ".png")
        #        print(today)
        if platform.system() == 'Windows':
            # 윈도우인 경우
            file = discord.File("./data/confim_korea.png", filename="image.png")
        else:
            # 우분투인 경우
            file = discord.File("/discord-bot/data/confim_korea.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=update)
        await message.channel.send(file=file,embed=embed)
        # await message.channel.send("할 말", embed=embed)  # embed와 일반메시지를 함께 보내고 싶으시면 이렇게 사용하시면 됩니다.

    if message.content == prefix + "격리해제":
        # 기본적으로 한국의 정보를 가져옴
        embed = discord.Embed(title=month + "월 " + day + "일" + " 코로나 상황", color=0x62c1cc)
        embed.add_field(name="누적 격리해제", value=korea.rescued + "명 ", inline=True)
        embed.add_field(name="금일 격리해제", value=korea.prev_rescured + "명 ", inline=True)
        embed.set_image(url="http://ncov.mohw.go.kr/static/image/main_chart/live_pdata2_" + today + ".png")
        embed.set_footer(text=update)
        await message.channel.send(embed=embed)

    if message.content == prefix + "세계":
        # 전세계의 정보를 가져옴
        country = "전세계"
        embed = discord.Embed(title=month + "월 " + day + "일 " + country + " 코로나 상황", color=0xa83232)
        embed.add_field(name="누적 확진자수",
                        value=world_data.w_confirmed + "명 :small_red_triangle:" + world_data.w_prev_confirmed,
                        inline=False)
        embed.add_field(name="격리중", value=world_data.w_active + "명", inline=False)
        embed.add_field(name="격리해제", value=world_data.w_rescued + "명", inline=False)
        embed.add_field(name="사망자", value=world_data.w_death + "명 :small_red_triangle:" + world_data.w_prev_death,
                        inline=False)
        if platform.system() == 'Windows':
            # 윈도우인 경우
            file = discord.File("./data/confim_world.png", filename="image.png")
        else:
            # 우분투인 경우
            file = discord.File("/discord-bot/data/confim_world.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=update)
        await message.channel.send(file=file,embed=embed)

    if message.content == prefix + "아시아":
        # 아시아의 정보를 가져옴
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

    if message.content == prefix + "유럽":
        # 유럽의 정보를 가져옴
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

    if message.content == prefix + "북아메리카":
        # 북미의 정보를 가져옴
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

    if message.content == prefix + "남아메리카":
        # 남미의 정보를 가져옴
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

    if message.content == prefix + "아프리카":
        # 아프리카의 정보를 가져옴
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

    if message.content == prefix + "오세아니아":
        # 오세아니아의 정보를 가져옴
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
    if message.content == prefix + "국가목록":
        embed = discord.Embed(title="명령어 목록", description="명령어 목록입니다.", color=0x62c1cc)
        embed.add_field(name="!한국", value="한국의 코로나 상황을 알려줍니다.", inline=False)
        embed.add_field(name="!현재상황", value="한국의 코로나 상황을 알려줍니다.", inline=False)
        embed.add_field(name="!격리해제", value="한국의 완치(격리해제) 상황을 알려줍니다.", inline=False)
        embed.add_field(name="!세계", value="전세계 코로나 확진자 정보를  알려줍니다.", inline=False)
        embed.add_field(name="!각나라별이름", value="[추가예정]각 나라별 코로나 상황을 알려줍니다.", inline=False)
        await message.channel.send(embed=embed)

    if message.content == prefix + "미국":
        print("요청")

        country = "미국"
        embed = discord.Embed(title=month + "월 " + day + "일 " + country + " 코로나 상황", color=0x62c1cc)
        embed.add_field(name="누적 확진자수", value=world_data.usa_confim + "명 :small_red_triangle:" +str(int(week.w_1_t_p)-int(week.w_1_1_p)),
                        inline=False)
        embed.add_field(name="격리해제", value=world_data.usa_resued + "명", inline=False)
        embed.add_field(name="격리중", value=world_data.usa_active + "명 :small_red_triangle:" + world_data.usa_prev_confim, inline=False)
        embed.add_field(name="사망자", value=world_data.usa_dead + "명 :small_red_triangle:" + world_data.usa_prev_dead, inline=False)
        #        print(today)
        if platform.system() == 'Windows':
            # 윈도우인 경우
            file = discord.File("./data/confim_usa.png", filename="image.png")
        else:
            # 우분투인 경우
            file = discord.File("/discord-bot/data/confim_usa.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        embed.set_footer(text=update)
        await message.channel.send(file=file,embed=embed)

        if message.content == prefix + "영국":
            print("요청")

            country = "영국"
            embed = discord.Embed(title=month + "월 " + day + "일 " + country + " 코로나 상황", color=0x62c1cc)
            embed.add_field(name="누적 확진자수", value=world_data.usa_confim + "명 :small_red_triangle:" + str(int(week.w_2_t_p)-int(week.w_2_1_p)),
                            inline=False)
            embed.add_field(name="격리해제", value=world_data.usa_resued + "명", inline=False)
            embed.add_field(name="격리중",
                            value=world_data.usa_active + "명 :small_red_triangle:" + world_data.usa_prev_confim,
                            inline=False)
            embed.add_field(name="사망자", value=world_data.usa_dead + "명 :small_red_triangle:" + world_data.usa_prev_dead,
                            inline=False)
            #        print(today)
            if platform.system() == 'Windows':
                # 윈도우인 경우
                file = discord.File("./data/confim_england.png", filename="image.png")
            else:
                # 우분투인 경우
                file = discord.File("/discord-bot/data/confim_england.png", filename="image.png")
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text=update)
            await message.channel.send(file=file, embed=embed)

        if message.content == prefix + "영국":
            print("요청")

            country = "영국"
            embed = discord.Embed(title=month + "월 " + day + "일 " + country + " 코로나 상황", color=0x62c1cc)
            embed.add_field(name="누적 확진자수", value=world_data.usa_confim + "명 :small_red_triangle:" + str(
                int(week.w_2_t_p) - int(week.w_2_1_p)),
                            inline=False)
            embed.add_field(name="격리해제", value=world_data.usa_resued + "명", inline=False)
            embed.add_field(name="격리중",
                            value=world_data.usa_active + "명 :small_red_triangle:" + world_data.usa_prev_confim,
                            inline=False)
            embed.add_field(name="사망자", value=world_data.usa_dead + "명 :small_red_triangle:" + world_data.usa_prev_dead,
                            inline=False)
            #        print(today)
            if platform.system() == 'Windows':
                # 윈도우인 경우
                file = discord.File("./data/confim_england.png", filename="image.png")
            else:
                # 우분투인 경우
                file = discord.File("/discord-bot/data/confim_england.png", filename="image.png")
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text=update)
            await message.channel.send(file=file, embed=embed)


client.run(token1)
