import requests

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

cookies = {
    'over18': '1'
}

res = requests.get(url, headers=headers, cookies=cookies)

print(res.text)