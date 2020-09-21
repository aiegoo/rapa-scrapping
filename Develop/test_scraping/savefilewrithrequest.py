import requests

url = 'http://blog.naver.com/otter35'
url = 'https://www.coupang.com/'

header = {'User-Agent': ''}

res = requests.get(url=url, headers=header)
print(type(res), res)


print(res.status_code)
if(res.status_code == 200):
    with open('datas/response01.html', 'w') as fp:
        fp.write(res.text)