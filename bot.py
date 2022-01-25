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
import random
#from chart import chart_world,chart_korea,chart_usa,chart_england,chart_belgium,chart_canada,chart_china,chart_france,chart_germany,chart_Indonesia,chart_iran,chart_italy,chart_japan,chart_nederlands,chart_philippines,chart_spain,chart_swiss,chart_thailand,chart_turky,chart_vietnam

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
    await bt(['!명령어 로 명령어를 확인할수 있습니다.','한국 확진자수 : ' + korea.confirmed + '명', '아시아 확진자수 : ' + world_data.as_confirmed + '명',
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
        embed = discord.Embed(title="명령어 목록", description="현재 사용할수있는 명령어입니다.", color=0x62c1cc)
        embed.add_field(name=":point_right:!마스크 '주소'", value="입력한 주소지의 공적마스크 판매처를 알려줍니다.", inline=False)
        embed.add_field(name=":point_right:!한국", value="한국의 코로나 상황을 알려줍니다.", inline=False)
        embed.add_field(name=":point_right:!정보출처", value="데이터를 가져오는 사이트를 알려줍니다.", inline=False)
        embed.add_field(name=":point_right:!홍보자료", value="방역수칙 이미지를 불러옵니다", inline=False)
        embed.add_field(name=":point_right:!세계", value="주요 확진국가의 코로나 확진자 정보를 알려줍니다.", inline=False)
        embed.add_field(name=":point_right:!'국가명'", value="각 확진국가들의 확진자 정보를 알려줍니다\n"+
                        "주요 확진국가들을 검색할수있습니다.(19개국)\n"+
                        "입력 예시) :point_right:!미국, !영국, !프랑스, !스페인 ....", inline=False)
        embed.add_field(name=":point_right:!아시아, !유럽, !북아메리카, !남아메리카, !아프리카, !오세아니아", value="각 대륙별 코로나 상황을 알려줍니다.", inline=False)
        await message.channel.send(embed=embed)
        # DM으로 메시지를 보냅니다.
        # await message.author.send("응답")


    if message.content == prefix + "정보출처":
        embed = discord.Embed(title="크롤링 정보 출처", description="현재 데이터를 가져오고있는 사이트들입니다.", color=0x62c1cc)
        embed.add_field(name="worldometers", value="https://www.worldometers.info/coronavirus/", inline=False)
        embed.add_field(name="보건복지부", value="http://ncov.mohw.go.kr/", inline=False)
        embed.add_field(name="공적마스크API", value="https://app.swaggerhub.com/apis-docs/Promptech/public-mask-info/20200307-oas3#/", inline=False)
        await message.channel.send(embed=embed)

    if message.content == prefix + "홍보자료":

        choice = random.randrange(1,8) # 7개면 >> (1,8)

        if choice == 1:

            embed = discord.Embed(title="생활속 거리두기 지침",color=0xff6969)
            embed2 = discord.Embed(title="생활속 거리두기 지침",color=0xff6969)
            if platform.system() == 'Windows':
                # 윈도우인 경우
                file = discord.File("./data/life_distance.png", filename="image.png")
                file2 = discord.File("./data/life_distance2.png", filename="image2.png")
            else:
                # 우분투인 경우
                file = discord.File("/discord-bot/data/life_distance.png", filename="image.png")
                file2 = discord.File("/discord-bot/data/life_distance2.png", filename="image2.png")

            embed.set_image(url="attachment://image.png")
            embed.set_footer(text="이미지출처 - 보건복지부")
            embed2.set_image(url="attachment://image2.png")
            embed2.set_footer(text="이미지출처 - 보건복지부")
            await message.channel.send(file=file, embed=embed)
            await message.channel.send(file=file2, embed=embed2)
            print("1!")

        if choice == 2:
            embed = discord.Embed(title="생활속 거리두기 실천", color=0xff6969)
            if platform.system() == 'Windows':
                # 윈도우인 경우
                file = discord.File("./data/how_do_life_diatance.png", filename="image.png")
            else:
                # 우분투인 경우
                file = discord.File("/discord-bot/data/how_do_life_diatance.png", filename="image.png")
            embed.add_field(name="링크", value="http://ncov.mohw.go.kr/guidelineView.do?brdId=6&brdGubun=61&dataGubun=612&ncvContSeq=2575&contSeq=2575&board_id=&gubun=", inline=False)
            embed.set_image(url="attachment://image.png")
            embed.set_footer(text="이미지출처 - 보건복지부")
            await message.channel.send(file=file, embed=embed)
            print("2!")
        if choice == 3:
            embed = discord.Embed(title="전자출입명부 (KI-Pass)", color=0xff6969)
            if platform.system() == 'Windows':
                # 윈도우인 경우
                file = discord.File("./data/my_qr.png", filename="image.png")
            else:
                # 우분투인 경우
                file = discord.File("/discord-bot/data/my_qr.png", filename="image.png")

            embed.set_image(url="attachment://image.png")
            embed.set_footer(text="이미지출처 - 보건복지부")
            await message.channel.send(file=file, embed=embed)
            print("3!")

        if choice == 4:
            embed = discord.Embed(title="긴급복지 의료비지원", color=0xff6969)
            if platform.system() == 'Windows':
                # 윈도우인 경우
                file = discord.File("./data/medical_assist.png", filename="image.png")
            else:
                # 우분투인 경우
                file = discord.File("/discord-bot/data/medical_assist.png", filename="image.png")

            embed.set_image(url="attachment://image.png")
            embed.set_footer(text="이미지출처 - 보건복지부")
            await message.channel.send(file=file, embed=embed)
            print("4!")

        if choice == 5:
            embed = discord.Embed(title="수도권 집단감염 대응", color=0xff6969)
            if platform.system() == 'Windows':
                # 윈도우인 경우
                file = discord.File("./data/warning.png", filename="image.png")
            else:
                # 우분투인 경우
                file = discord.File("/discord-bot/data/warning.png", filename="image.png")

            embed.set_image(url="attachment://image.png")
            embed.set_footer(text="이미지출처 - 보건복지부")
            await message.channel.send(file=file, embed=embed)
            print("5!")

        if choice == 6:
            embed = discord.Embed(title="감염병 스트레스 극복", color=0xff6969)
            if platform.system() == 'Windows':
                # 윈도우인 경우
                file = discord.File("./data/stress_tel.png", filename="image.png")
            else:
                # 우분투인 경우
                file = discord.File("/discord-bot/data/stress_tel.png", filename="image.png")

            embed.set_image(url="attachment://image.png")
            embed.set_footer(text="이미지출처 - 보건복지부")
            await message.channel.send(file=file, embed=embed)
            print("6!")

        if choice == 7:
            embed = discord.Embed(title="생활속 거리두기 핵심수칙 5가지", color=0xff6969)
            if platform.system() == 'Windows':
                # 윈도우인 경우
                file = discord.File("./data/rule5.png", filename="image.png")
            else:
                # 우분투인 경우
                file = discord.File("/discord-bot/data/rule5.png", filename="image.png")

            embed.set_image(url="attachment://image.png")
            embed.set_footer(text="이미지출처 - 보건복지부")
            await message.channel.send(file=file, embed=embed)
            print("7!")

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
        #emoji = 'U+003AU+0066U+006CU+0061U+0067U+005FU+006BU+0072U+003A'
        await message.channel.send(embed=embed)
        await message.add_reaction('a:flag_kr:b57d2718c0f2330c0e06166d4b5fb606')


        async def on_reaction_add(reaction, user):
            if reaction.emoji == ':flag_kr:':
                message.reaction(':flag_kr:')
                message.reaction(':globe_with_meridians:')



    if message.content.startswith(prefix + "마스크"):
        split_addr = message.content.split(maxsplit=2)
        print(split_addr)
        len_addr = len(split_addr)
        print(len_addr)
        if len_addr == 1:
            embed = discord.Embed(title="공적 마스크 판매처 조회방법",
                                  description="'!마스크 서울시 양천구 신월동' 과 같이 주소를 입력해주세요\n" +
                                              "동의 경우 신월2동이면 신월동으로 입력함.\n" +
                                              "주소 입력 예시 >> 서울시 양천구 신월동 , 부산시 북구 구포동 \n"+
                                              "제주도는 '제주시,제주도,제주특별자치도 연동' 과 같이 입력해주세요", color=0x9fd6f4)
            await message.channel.send(embed=embed)
        if split_addr[1] =='서울시':
            split_addr[1] = '서울특별시 '
        elif split_addr[1] =='인천시':
            split_addr[1] = '인천광역시 '
        elif split_addr[1] == '부산시':
            split_addr[1] = '부산광역시 '
        elif split_addr[1] == '광주시':
            split_addr[1] = '광주광역시 '
        elif split_addr[1] == '대전시':
            split_addr[1] = '대전광역시 '
        elif split_addr[1] == '울산시':
            split_addr[1] = '울산광역시 '
        elif split_addr[1] == '제주시':
            split_addr[1] ='제주특별자치도 제주시 '
        elif split_addr[1] == '제주도':
            split_addr[1] ='제주특별자치도 제주시 '
        elif split_addr[1] == '제주특별자치도':
            split_addr[1] ='제주특별자치도 제주시 '
        print(split_addr)
        mask_addr = "".join(str(split_addr[1])+str(split_addr[2]))
        print(mask_addr)
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
        stop = []
        stop_c = []
        stop_sell = 0
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

        #d = ['월', '화', '수', '목', '금', '토', '일']
        #y = datetime.today().weekday()
        #print(d[y])
        #if y == 0:
        #    buy_mask = '주민번호 끝자리 1,6년생'
        #elif y == 1:
        #    buy_mask = '주민번호 끝자리 2,7년생'
        #elif y == 2:
        #    buy_mask = '주민번호 끝자리 3,8년생'
        #elif y == 3:
        #    buy_mask = '주민번호 끝자리 4,9년생'
        #elif y == 4:
        #    buy_mask = '주민번호 끝자리 5,0년생'
        #elif y == 5:
        #    buy_mask = '모든사람'
        #elif y == 6:
        #    buy_mask = '모든사람'

        embed = discord.Embed(title=month + "월 " + day + "일 " + " 마스크 상황",
                              description="6월 1일부터 마스크 5부제 폐지로 인해 \n "+
                                          "주중 18세이하는 5장, 성인은 3장씩 구매 가능합니다\n"
                                          + '판매 중지 '+str(cnt_stop)+'곳을 제외한 ' + str(int(store_count)-int(cnt_stop)) + '곳에서 구매 가능합니다.\n'
                                          + '전체목록 지도 : ' + short_url, color=0x9fd6f4)
        embed.set_footer(text="기준 주소 : " + str(mask_addr))
        await message.channel.send(embed=embed)

    if message.content == prefix + "한국":

        country = "한국"
        embed = discord.Embed(title=month + "월 " + day + "일 " + country + " 코로나 상황", color=0x62c1cc)
        embed.add_field(name="누적 확진자수", value=korea.confirmed + "명 :small_red_triangle:" + korea.prev_confimed,
                        inline=False)
        embed.add_field(name="격리해제", value=korea.rescued + "명 :small_red_triangle:" + korea.prev_rescured, inline=False)
        embed.add_field(name="격리중", value=korea.cure + "명", inline=False)
        embed.add_field(name="사망자", value=korea.dead + "명 :small_red_triangle:" + korea.prev_death, inline=False)
        embed.add_field(name="검사대비 확진률", value=korea.kr_confim_percent + "%", inline=False)
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


client.run(token1)
