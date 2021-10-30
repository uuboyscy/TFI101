import requests

url = 'http://ec2-54-249-185-80.ap-northeast-1.compute.amazonaws.com/hello_post'

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

data = {
    'username': 'vuchzvichzjkfbdhajkhfdsk',
    'aaa': 'yvz8ovhucizxl'
}

res = requests.post(url, headers=headers, data=data)
# print(res.text)

url = 'http://httpbin.org/post?a=123&b=456'

res = requests.post(url, headers=headers, data=data)
print(res.text)