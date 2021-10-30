import requests
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

articleUrl = 'https://www.ptt.cc/bbs/movie/M.1635525796.A.C08.html'

resArticle = requests.get(articleUrl, headers=headers)

soupArticle = BeautifulSoup(resArticle.text, 'html.parser')

articleContent = soupArticle.select('div[id="main-content"]')[0]

print(articleContent.text.split('※ 發信站')[0])