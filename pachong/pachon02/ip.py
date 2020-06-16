from urllib import request
from lxml import etree
mainip=request.urlopen('http://www.httpbin.org/ip').read().decode()
#采集 ip
dic={}
for i in range(1,10):
    url='https://www.xicidaili.com/nn/{}'.format(i)
    heads={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    heads1=request.Request(url,headers=heads)
    res=request.urlopen(heads1).read().decode()
    ipresult=etree.HTML(res).xpath('//tr[@class="odd"]/td[2]/text()')
    duankou=etree.HTML(res).xpath('//tr[@class="odd"]/td[3]/text()')
    leixin=etree.HTML(res).xpath('//tr[@class="odd"]/td[6]/text()')
    # print(ipresult,leixin)
    zip(leixin,ipresult,duankou)
    for i in zip(leixin,ipresult,duankou):
        dic[i[0]]=i[1]+':'+i[2]
        handler=request.ProxyHandler(dic)
        opener=request.build_opener(handler)
        res=opener.open('http://www.httpbin.org/ip').read().decode()
        if res!=mainip:
            print('可用ip%s'%res)
            with open('ipdali.txt','a',encoding='utf-8') as w:
                w.write(str(res))
        dic={}




