from urllib import request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

url = 'https://www.ptt.cc/bbs/joke/index.html'

req = request.Request(url=url, headers=headers)
res = request.urlopen(req)

html = res.read().decode('utf-8')

# print(html)

soup = BeautifulSoup(html, 'html.parser') # xml -> lxml

# print(soup)

# logo = soup.findAll('a', {'id': 'logo'}) # [<a href="/bbs/" id="logo">批踢踢實業坊</a>]
logo = soup.findAll('a', id='logo')
print(logo[0]) # <a href="/bbs/" id="logo">批踢踢實業坊</a>
print(logo[0].text) # 批踢踢實業坊
print("https://www.ptt.cc" + logo[0]['href'])

board = soup.findAll('a', class_='board')
print(board[0])

print('=============')

# topbar = soup.select('div[id="topbar"]')
topbar = soup.select('div#topbar')
print(topbar[0])
print('------')
print(topbar[0].select('a'))
for i in topbar[0].findAll('a'):
    print(i)

print('=============')

print(type(soup))
print(type(topbar[0]))

