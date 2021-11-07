import requests
from bs4 import BeautifulSoup

url = 'http://ec2-54-64-129-1.ap-northeast-1.compute.amazonaws.com/practice/cfi101-99'

headers = {'user-agent': '123'}

ss = requests.session()

res = ss.get(url, headers=headers)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
key = soup.select('input')[1]['name']
value = soup.select('input')[1]['value']
# print(key, value)

data = {key: value, 'pwd': '施丞優'}
res = ss.post(url, data=data, headers=headers)
print(res.text)
