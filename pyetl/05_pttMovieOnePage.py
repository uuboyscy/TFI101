import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

url = 'https://www.ptt.cc/bbs/movie/index.html'

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

# print(soup)

titleSoupList = soup.select('div[class="title"]')
# print(titleSoupList)
for titleSoup in titleSoupList:
    # titleSoup.select('a')
    # -> [<a href="/bbs/movie/M.1635525796.A.C08.html">Re: [好無雷] 怒火 ：經典港片打出新高度</a>]
    title = titleSoup.select('a')[0].text
    articleUrl = "https://www.ptt.cc" + titleSoup.select('a')[0]['href']
    print(title)
    print(articleUrl)
    print('=====')