import requests
import json
import time
from bs4 import BeautifulSoup

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

url = 'https://buzzorange.com/techorange/wp/wp-admin/admin-ajax.php'

dataStr = """action: ceris_posts_listing_grid
args[post_type]: post
args[ignore_sticky_posts]: 1
args[post_status]: publish
args[posts_per_page]: 8
args[offset]: 0
args[orderby]: date
postOffset: 8
type: loadmore
moduleInfo[post_source]: all
moduleInfo[post_icon]: disable
moduleInfo[iconPosition]: top-right
moduleInfo[post_icon_animation]: disable
moduleInfo[bookmark]: off
securityCheck: 8e2a7071cd"""

data = {r.split(': ')[0]: r.split(': ')[1] for r in dataStr.split('\n')}
# print(data)

for i in range(0, 3):
    print('[{}]'.format(i))
    res = requests.post(url, headers=headers, data=data)
    # print(res.json())
    soup = BeautifulSoup(res.json(), 'html.parser')

    ## Get title information
    ## h3 class="post__title typescale-2" a
    titleSoupList = soup.select('h3[class="post__title typescale-2"]')
    for titleSoup in titleSoupList:
        title = titleSoup.a.text ## equal to .select_one('a').text
        articleUrl = titleSoup.a['href']
        # print(titleSoup)
        print(title)
        print(articleUrl)
        print('===')

    data['postOffset'] = str(int(data['postOffset']) + 8)

    time.sleep(5)