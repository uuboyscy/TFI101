import requests
import json
import ssl
import os
from urllib import request
ssl._create_default_https_context=ssl._create_unverified_context

if not os.path.exists('./dcardphoto'):
    os.mkdir('./dcardphoto')

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

"""
[{'id': 'b7be573c-e813-45ae-af02-197f8eae234d', 'url': 'https://i.imgur.com/e4EUH5Q.jpg', 'normalizedUrl': 'https://imgur.com/e4EUH5Q', 'thumbnail': 'https://i.imgur.com/e4EUH5Ql.jpg', 'type': 'image/imgur', 'tags': ['ANNOTATED'], 'createdAt': '2021-10-17T12:56:43.098Z', 'updatedAt': '2021-10-17T13:00:33.042Z', 'width': 2320, 'height': 3480, 'croppingWindow': {'anchorX': 0, 'anchorY': 464, 'width': 2320, 'height': 1392}}, {'id': '17311e4e-f377-4da2-96c3-a8dd152daf62', 'url': 'https://i.imgur.com/2J2y8eu.jpg', 'normalizedUrl': 'https://imgur.com/2J2y8eu', 'thumbnail': 'https://i.imgur.com/2J2y8eul.jpg', 'type': 'image/imgur', 'tags': ['ANNOTATED'], 'createdAt': '2021-10-17T12:56:43.098Z', 'updatedAt': '2021-10-17T13:00:33.042Z', 'width': 6960, 'height': 4640}, {'id': '8bd133c6-6a99-4b22-89e0-c7c7e82e7105', 'url': 'https://i.imgur.com/fSl1lr4.jpg', 'normalizedUrl': 'https://imgur.com/fSl1lr4', 'thumbnail': 'https://i.imgur.com/fSl1lr4l.jpg', 'type': 'image/imgur', 'tags': ['ANNOTATED'], 'createdAt': '2021-10-17T12:56:43.098Z', 'updatedAt': '2021-10-17T13:00:33.042Z', 'width': 5568, 'height': 3712}, {'id': 'c13e24c7-d070-4fd0-b1f9-a033f0314591', 'url': 'https://i.imgur.com/N72O25D.jpg', 'normalizedUrl': 'https://imgur.com/N72O25D', 'thumbnail': 'https://i.imgur.com/N72O25Dl.jpg', 'type': 'image/imgur', 'tags': ['ANNOTATED'], 'createdAt': '2021-10-17T12:56:43.098Z', 'updatedAt': '2021-10-17T13:00:33.042Z', 'width': 3712, 'height': 5568}, {'id': 'bfa88711-414f-4308-8eb2-7f299af1ba14', 'url': 'https://i.imgur.com/ujHmaAP.jpg', 'normalizedUrl': 'https://imgur.com/ujHmaAP', 'thumbnail': 'https://i.imgur.com/ujHmaAPl.jpg', 'type': 'image/imgur', 'tags': ['ANNOTATED'], 'createdAt': '2021-10-17T12:56:43.098Z', 'updatedAt': '2021-10-17T13:00:33.042Z', 'width': 4176, 'height': 2784}]
"""
print(jsonData[1]['mediaMeta'])
for i in jsonData[1]['mediaMeta']:
    print(i)

for articleObj in jsonData:
    title = articleObj['title']
    articleUrl = 'https://www.dcard.tw/f/photography/p/' + str(articleObj['id'])
    print(title)
    print(articleUrl)
    ## imgObj -> {'id': 'b7be573c-e813-45ae-af02-197f8eae234d', 'url': 'https://i.imgur.com/e4EUH5Q.jpg', 'normalizedUrl': 'https://imgur.com/e4EUH5Q', 'thumbnail': 'https: ...
    for idx, imgObj in enumerate(articleObj['mediaMeta']):
        imgUrl = imgObj['url']
        try:
            imgLocalPath = './dcardphoto/{}_{}.{}'.format(title.replace('/', ''),
                                                           idx,
                                                           imgUrl.split('.')[-1])
            # request.urlretrieve(imgUrl, imgLocalPath)
            resImg = requests.get(imgUrl, headers=headers)
            with open(imgLocalPath, 'wb') as f:
                f.write(resImg.content)
        except:
            pass
        print('\t', imgUrl)
    print('=======')

