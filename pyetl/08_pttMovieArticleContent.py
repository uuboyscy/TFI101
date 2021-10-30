import os
import requests
from bs4 import BeautifulSoup
import time
import random

if not os.path.exists('./pttMovie'):
    os.mkdir('./pttMovie')

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

url = 'https://www.ptt.cc/bbs/movie/index.html'

for i in range(0, 5):
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    # print(soup)

    titleSoupList = soup.select('div[class="title"]')
    # print(titleSoupList)
    for titleSoup in titleSoupList:
        # titleSoup.select('a')
        # -> [<a href="/bbs/movie/M.1635525796.A.C08.html">Re: [好無雷] 怒火 ：經典港片打出新高度</a>]
        try:
            time.sleep(random.randint(1, 50)/10)
            title = titleSoup.select('a')[0].text
            articleUrl = "https://www.ptt.cc" + titleSoup.select('a')[0]['href']
            # Get article content
            resArticle = requests.get(articleUrl, headers=headers)
            soupArticle = BeautifulSoup(resArticle.text, 'html.parser')
            articleContent = soupArticle.select('div[id="main-content"]')[0].text.split('※ 發信站')[0]
            try:
                with open('./pttMovie/{}.txt'.format(title), 'w', encoding='utf-8') as f:
                    f.write(articleContent)
            except FileNotFoundError:
                with open('./pttMovie/{}.txt'.format(title.replace('/', '')), 'w', encoding='utf-8') as f:
                    f.write(articleContent)
            except OSError:
                pass

            print(title)
            print(articleUrl)
        except IndexError as e:
            print(e)
        print('=====')

    url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]['href']
