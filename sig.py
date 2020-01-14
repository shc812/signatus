import discord
import asyncio
import random
import os
 
client = discord.Client()
 
# 생성된 토큰을 입력해준다.
#token = " "


# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    game = discord.Game("사용법은 !설명 입력")
    await client.change_presence(status=discord.Status.idle, activity=game)
    print("================")

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None
    if message.content.startswith('!시작'):
        channel = message.channel 
        #msg = await client.wait_for('message', timeout=30)
        #lenp = int(msg.content)
        await channel.send('경매에 참여하는 인원들을 /로 구분하여 입력해주세요\n예시) 병샷/빙샷/풀캐/수상한/알수없음/나도몰라\n입력하지 않거나 제대로 입력하지 않으면 고장날지도 몰라요...ㅠㅠ')
        msg2 = await client.wait_for('message', timeout=60)
        arrr = str(msg2.content).split('/')
        lenp = len(arrr)
        rewardList = ['각인서','미스트리움','아크숨결','어빌스톤','장비상자']

        if lenp == 8:
            rewardList.append('꽝')
            rewardList.append('꽝')
            rewardList.append('꽝')
        elif lenp == 7:
            rewardList.append('꽝')
            rewardList.append('꽝')
        elif lenp == 6:
            rewardList.append('꽝')

        # 1수
        random.shuffle(rewardList)
        await channel.send('<1수>\n')
        num=-1
        for peo in arrr:
            num=num+1
            await channel.send(peo+' : '+rewardList[num]+'\n')
        await channel.send('=============\n')
        # 2수
        random.shuffle(rewardList)
        await channel.send('<2수>\n')
        num=-1
        for peo in arrr:
            num=num+1
            await channel.send(peo+' : '+rewardList[num]+'\n')
        await channel.send('=============\n')
        # 3수
        random.shuffle(rewardList)
        await channel.send('<3수>\n')
        num=-1
        for peo in arrr:
            num=num+1
            await channel.send(peo+' : '+rewardList[num]+'\n')
        await channel.send('=============\n')

        rewardList = ['각인서','미스트리움','아크숨결','어빌스톤','장비상자']
    elif message.content.startswith('!'):

        if message.content.startswith('!설명'):
            channel = message.channel
            await channel.send('저의 주인 병샷님에 의해 제작되었습니다.\n<현재기능>\n!키워드 대화(!안녕,!주사위,!강화,재련,제련 등)\n미스틱경매 사다리타기 : !시작')

        elif message.content.startswith('!안녕'):
            channel = message.channel
            await channel.send('안녕하세요 시그에요')
        elif message.content.startswith('!왜'):
            channel = message.channel
            await channel.send('묻지마세요 모르니깐요')
        elif message.content.startswith('!바보'):
            channel = message.channel
            await channel.send('제가 더 똑똑할 것 같아요!^0^')
        elif message.content.startswith('!조용'):
            channel = message.channel
            await channel.send('쉿! 0ㅅ0')
        elif message.content.startswith('!닥'):
            channel = message.channel
            await channel.send('↖^0^↗')
        elif message.content.startswith('!심심'):
            channel = message.channel
            await channel.send('제가 더 심심해요. 메시지를 계속 주시해야하는 제 기분을 아시나요?')
        elif message.content.startswith('!놀아'):
            channel = message.channel
            await channel.send('싫어요')
        elif message.content.startswith('!나가'):
            channel = message.channel
            await channel.send('안돼요!')
        elif message.content.startswith('!일'):
            channel = message.channel
            await channel.send('ㅡ,ㅡ')
        elif message.content.startswith('!이'):
            channel = message.channel
            await channel.send('ㅡ,ㅡ?;;')
        elif message.content.startswith('!주사위'):
            channel = message.channel
            randd = int(round(random.random(),2)*100)
            randdd = str(randd)
            await channel.send('짠! '+randdd+' 나왔습니다.')
        elif message.content.startswith('!강화'):
            channel = message.channel
            if random.random()>0.8 :
                await channel.send('지금이에요 질러요!!!!!!(도망)')
            else :
                await channel.send('장기백씨가 문을 두드리고 있는것 같아요!')
        elif message.content.startswith('!재련'):
            channel = message.channel
            if random.random()>0.8 :
                await channel.send('지금이 타이밍같습니다! 아님 말고요')
            else :
                await channel.send('장기백씨와 면담이 필요할 것 같습니다.')
        elif message.content.startswith('!제련'):
            channel = message.channel
            if random.random()>0.8 :
                await channel.send('빰빰 빠바빰~~')
            else :
                await channel.send('빰빰 빠바빰~~(남의 강화성공 소리)')
        else:
            channel = message.channel
            if random.random()>0.8 :
                await channel.send(':worried:')
            elif random.random()>0.6:
                await channel.send(':face_with_raised_eyebrow:')
            elif random.random()>0.4:
                await channel.send(':flushed:')
            elif random.random()>0.6:
                await channel.send(':rolling_eyes:')
            else:
                await channel.send(':confounded:')
            
    
    else:
        if message.content.startswith('사다리'):
            channel = message.channel
            await channel.send('사용법은 !설명 을 입력해보세요')

        if message.content.startswith('시그'):
            channel = message.channel
            await channel.send('사다리타기는 저한테 맡겨주세요. 다른 기능은 개발중이죠. !설명 을 입력해보세요')

        if message.content.startswith('ㅠㅠㅠ'):
            channel = message.channel
            await channel.send('울지마세요 ㅠㅠ')
        
        if message.content.startswith('ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ'):
            channel = message.channel
            await channel.send('웃다가 쓰러지겠어요~ㅎㅎ')
        elif message.content.startswith('ㅋㅋㅋㅋㅋㅋㅋㅋ'):
            channel = message.channel
            await channel.send('왜 웃는거죠? 알려주세요^0^')
        elif message.content.startswith('ㅋㅋㅋㅋ'):
            channel = message.channel
            await channel.send(message.content+'ㅋㅋㅋ')

        if message.content.startswith('샷'):
            channel = message.channel
            await channel.send('주인님 바빠요(혹시 자고있을지도..)')
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
