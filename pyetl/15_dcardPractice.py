import requests
import json

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=237247011'

res = requests.get(url, headers=headers)

# print(res.text)
jsonData = json.loads(res.text) # List of article object

# for i in jsonData:
#     print(i)
# for k in jsonData[0]:
#     print(k)
# print(jsonData[0].keys())

for articleObj in jsonData:
    title = articleObj['title']
    articleUrl = 'https://www.dcard.tw/f/photography/p/' + str(articleObj['id'])
    print(title)
    print(articleUrl)
    print('=======')