from urllib import request

url = 'http://ec2-54-249-185-80.ap-northeast-1.compute.amazonaws.com/hello_get?name=Allen&age=22'

res = request.urlopen(url=url)

print(res.read().decode('utf-8'))