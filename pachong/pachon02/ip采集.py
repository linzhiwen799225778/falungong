from urllib import request

url='http://www.httpbin.org/ip'
# res=request.urlopen(url).read().decode()
#res39.166.98.63本机ip


#从网站爬取ip
ipurl='https://www.xicidaili.com/nn/'
res0=request.urlopen(url=ipurl).read().decode()

#换ip发请求
ip={'http':'ip:port'}
iphander=request.ProxyHandler(ip)
opener=request.build_opener(iphander)
ipres=opener.open(url).read().decode()








