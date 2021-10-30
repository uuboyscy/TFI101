import requests
from bs4 import BeautifulSoup

landingUrl = 'https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'
over18Url = 'https://www.ptt.cc/ask/over18'
pttUrl = 'https://www.ptt.cc/bbs/Gossiping/index.html'

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

ss = requests.session()
data = dict()
print(ss.cookies)

resLanding = ss.get(landingUrl, headers=headers)
print(ss.cookies)
soupLanding = BeautifulSoup(resLanding.text, 'html.parser')
inputSoup = soupLanding.select('input')[0]
# print(inputSoup)
data[inputSoup['name']] = inputSoup['value']
# print(data)
buttonSoup = soupLanding.select('button')[0]
# print(buttonSoup)
data[buttonSoup['name']] = buttonSoup['value']
print(data)

ss.post(over18Url, headers=headers, data=data)
print(ss.cookies)

res = ss.get(pttUrl, headers=headers)
print(res.text)

