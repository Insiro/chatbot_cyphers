from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

defualtList=['랭킹','전적검색','오싸','아이템검색']

def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons':defualtList
    })
status =0
status2=0
season=13
charactor={'로라스':'roras','휴톤':'huton','루이스':'louis','타라':'tara','트리비아':'trivia','카인':'cain',
           '레나':'rena','드렉슬러':'drexler','도일':'doyle','토마스':'thomas','나이오비':'niobe','시바포':'shiva',
           '시바':'shiva','시바 포':'shiva','웨슬리':'wesley','스텔라':'stella','엘리셔':'alicia','클레어':'clare',
           '다이무스':'deimus','이글':'eagle','미를렌':'marlene','샬럿':'charlotte','윌라드':'willard','레이튼':'lleyton',
           '미쉘':'michelle','린':'rin','빅터':'viktor','카를로스':'carlos','호타루':'hotaru','트릭시':'trixie',
           '히카로드':'ricardo','까미유':'camille','자네트':'jannette','피터':'peter','아이작':'issac','레베카':'rebecca',
           '엘리':'ellie','마틴':'martin','브로스':'bruce','미아':'mia','드니스':'denise','제레온':'gereon','루시':'lucy',
           '티엔':'tian','하랑':'harang','J':'j','j':'j','제이':'j','벨져':'belzer','리첼':'richel','리사':'risa',
           '릭':'rick','제키엘':'jekiel','탄야':'tanya','캐럴':'carol','라이샌더':'lysander','루드빅':'ludwig','멜빈':'melvin',
           '디아나':'diana','클리브':'clive','헬레나':'helena','에바':'eva','론':'ron','레오노르':'leonor','시드니':'sidney'

           }
def btnRespone(respone,botton):
    return JsonResponse({
        'message':{'text':respone},
        'keyboard':{
            'type':'buttons',
            'buttons':[botton]
        }
    })
def textRespone(respone):
    return JsonResponse({
        'message':{
            'text':respone
        },
        'keyboard':{
            'type':'text'
        }
    })

def mainSelect(data):
    if data=='랭킹':
        status='랭킹'
        return btnRespone('어떤 랭킹을 조회하시겠습니까',['통합','투신','캐릭터'])
    elif data=='전적검색':
        status='전적'
        return textRespone('닉네임을 입력하시오')
    elif data=='오싸':
        status='0'
        contents='오싸'
        return btnRespone(contents,defualtList)

def rankSelect(data):
    global status
    if data=='통합':
        status='통합'
        status2=0
        contents = '상위 50위 조회하시겠습니까/n개인랭킹 검색하시겠습니까'
        return btnRespone(contents, ['전체랭킹', '개인랭킹'])
    elif data=='투신':
        status=0
        contents='투신'
        return btnRespone(contents,defualtList)
    elif data=='캐릭터':
        status='캐릭랭킹'
        return textRespone('어떤 캐릭터의 랭킹을 조회하겠습니까')


def allRank(data):
    if data == '전체랭킹':
        global status,status2
        status = 0
        status2=0
        link = 'article/ranking/total/' + season + '1'
        contents = parse(link, 0)
    elif data == '개인랭킹':
        if status2==2:
            link = link = 'article/ranking/total/' + season + '1/search/nickname' + data + '/1'
            contents = parse(link, 1)
        else:
            status2 = 2
            return textRespone('닉네임을 입력하시오')
    return btnRespone(contents, defualtList)

def charhistory(data):
    global status2
    global status
    global char
    if status2 == 1:
        if data == '전체랭킹':
            status2 = 0
            status = 0
            link = 'article/ranking/charac/' + season  +'/'+char+'/win/day/1'
            contents = parse(link,0)
        elif data == '개인랭킹':
            status2 = 2
            return textRespone('닉네임을 입력하시오')
    elif status2 == 2:
        link = link = 'article/ranking/total/' + season +'/'+char+'/win/day/search/'+data
        contents = parse(link,1)
    elif status2 == 0:
        status2 = 1
        char=data
        contents = '상위 50위 조회하시겠습니까/n개인랭킹 검색하시겠습니까'
        return btnRespone(contents, ['전체랭킹', '개인랭킹'])
    return btnRespone(contents, defualtList)

def history(data):
    global status
    status=0
    link='http://cyphers.nexon.com/cyphers/game/log/search/1/'+data
    contents=parse2(link)
    return btnRespone(contents,defualtList)

def parse2(data):
    #전적
    return 'test 전적'

def parse3():
    link='http://cyphers.nexon.com/cyphers/article/today'
    #오싸
    return 'test 오싸'

def parse(data,log):
    #long==0 : all

    link='http://cyphers.nexon.com/cyphers/'+data
    #랭킹
    return ;'test 랭킹'

@csrf_exempt

def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
    global status
    if status==0 :
        return mainSelect(datacontent)
    elif status=='랭킹' :
        return rankSelect(datacontent)
    elif status=='캐릭랭킹':
        return charhistory(datacontent)
    elif status=='전적':
        return history(datacontent)
    elif status=='통합':
        return allRank(datacontent)

