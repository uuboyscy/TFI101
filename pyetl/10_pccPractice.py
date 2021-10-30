import requests
from bs4 import BeautifulSoup

url = 'https://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance'

userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
headers = {
    'User-Agent': userAgent
}

dataStr = """method: search
searchMethod: true
searchTarget: ATM
orgName: hvjckxzlh
orgId: hvjczhlkcvx
hid_1: 1
tenderName: fdusahfd
tenderId: ygviuxcgzuy
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 110/10/30
awardAnnounceEndDate: 110/10/30
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: hrjtkh
hid_2: 1
gottenVendorName: vchxuoi
gottenVendorId: 
hid_3: 1
submitVendorName: 
submitVendorId: 
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢"""
data = {r.split(': ')[0]: r.split(': ')[1] for r in dataStr.split('\n')}
# print(data)

tmpUrl = 'https://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=ATM'

res = requests.get(tmpUrl, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

for i in soup.select('input[type="hidden"]'):
    # print(i)
    # print('=======')
    try:
        data[i['name']] = i['value']
    except:
        pass
print(data)

res = requests.post(url, headers=headers, data=data)
soup = BeautifulSoup(res.text, 'html.parser')

print(soup)

