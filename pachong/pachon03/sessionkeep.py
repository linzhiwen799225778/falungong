import requests
url='http://www.httpbin.org/cookies'
print(requests.get(url).text)
cookies={'ni':'wo'}
s=requests.session()
s.cookies.update(cookies)
s.cookies.headers(cookies)
print(s.get(url).text)