import requests
from bs4 import BeautifulSoup
link = 'http://cyphers.nexon.com/cyphers/article/ranking/total/13/1/'
req = requests.get(link)
html = req.text

soup = BeautifulSoup(html, 'html.parser')
soups = soup.select(
    '#rankTotalForm > div.rank_board.total_rank.mar_b10 > table > tbody > tr')
for tag in soup.select('#rankTotalForm > div.rank_board.total_rank.mar_b10 > table > tbody > tr > td'):
    print(tag.text.strip())

# for tag in soup.select('div[class=tit3]'):
 #   print(tag.text)


soups2 = soup.select(
    '#rankTotalForm > div.rank_board.total_rank.mar_b10 > table > tbody > tr:nth-child(1)')

def parseHistory(data):
    link = 'http://cyphers.nexon.com/cyphers/game/log/search/1/' + data
    return 'test 전적'

def parseRank(data):
    link = 'http://cyphers.nexon.com/cyphers/' + data
    soup = BeautifulSoup(html, 'html.parser')

    str1 = ''
    str2 = ''
    strs = ''
    j = 1
    i = 0
    for tag in soup.select('#rankTotalForm > div.rank_board.total_rank.mar_b10 > table > tbody > tr > td'):
        if j == 51:
            break
        i += 1
        if i == 2:
            str1 = str(j) + ' ' + tag.text[0:7]
        elif i == 3:
            str1 = str1 + ' ' + tag.text
        elif i == 4:
            str1 = str1 + ' ' + tag.text
        elif i == 5:
            i = 0
            j += 1
            if j != 51:
                str1 += '\n'
            str2 += str1


    return 'test 캐릭 or투신or통합 랭킹'
