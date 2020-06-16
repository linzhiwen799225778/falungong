from urllib import request
from lxml import etree
import gzip,re
num=0
url = "https://maoyan.com/board/4"
headers = {
'Cookie': '__mta=219111078.1588072392456.1588083937839.1588084114205.24; uuid_n_v=v1; uuid=3E27D9A0894111EAA1C98B1F174282C890E7C17DC1EF4824A8E836D01CA841A7; _lxsdk_cuid=171c07da3777f-0e736f17c06bc6-3a65420e-100200-171c07da378c8; _lxsdk=3E27D9A0894111EAA1C98B1F174282C890E7C17DC1EF4824A8E836D01CA841A7; t_lxid=171c07da52a1b-01f3ccf626f778-3a65420e-100200-171c07da52bc8-tid; mojo-uuid=77c61233368b7b1ad4e30a0aae285262; mojo-session-id={"id":"998f36a10d7ed624e877cdc6b909b8d7","time":1588079881557}; _csrf=57fde721c93a22876c35a0b442da3d0877526e07b5b440b37647f10d39035050; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1588072391,1588076777,1588083704,1588084099; __mta=219111078.1588072392456.1588083937839.1588084112321.24; mojo-trace-id=34; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1588084114; _lxsdk_s=171c0efe962-229-b9-eb4%7C%7C56',
# 'Cookie': '__mta=219111078.1588072392456.1588076786133.1588076871113.9; uuid_n_v=v1; uuid=3E27D9A0894111EAA1C98B1F174282C890E7C17DC1EF4824A8E836D01CA841A7; _csrf=1fc831273f713cdae1d145be9a8cc036bd14a03bcd4e08a12bd24058d6cfee6f; _lxsdk_cuid=171c07da3777f-0e736f17c06bc6-3a65420e-100200-171c07da378c8; _lxsdk=3E27D9A0894111EAA1C98B1F174282C890E7C17DC1EF4824A8E836D01CA841A7; t_lxid=171c07da52a1b-01f3ccf626f778-3a65420e-100200-171c07da52bc8-tid; mojo-uuid=77c61233368b7b1ad4e30a0aae285262; mojo-session-id={"id":"6cea331495a2ca5f1f47ced1eb1acff7","time":1588075060311}; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1588072391,1588076777; __mta=219111078.1588072392456.1588075711746.1588076781407.10; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1588076870; mojo-trace-id=18; _lxsdk_s=171c0a65690-38c-554-d1c%7C%7C32',
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
}
headers1 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'maoyan.com',
    'Referer': 'https://maoyan.com/board/4',
    'Upgrade-Insecure-Requests': '1',
    'Cookie': '__mta=219111078.1588072392456.1588076786133.1588076871113.9; uuid_n_v=v1; uuid=3E27D9A0894111EAA1C98B1F174282C890E7C17DC1EF4824A8E836D01CA841A7; _csrf=1fc831273f713cdae1d145be9a8cc036bd14a03bcd4e08a12bd24058d6cfee6f; _lxsdk_cuid=171c07da3777f-0e736f17c06bc6-3a65420e-100200-171c07da378c8; _lxsdk=3E27D9A0894111EAA1C98B1F174282C890E7C17DC1EF4824A8E836D01CA841A7; t_lxid=171c07da52a1b-01f3ccf626f778-3a65420e-100200-171c07da52bc8-tid; mojo-uuid=77c61233368b7b1ad4e30a0aae285262; mojo-session-id={"id":"6cea331495a2ca5f1f47ced1eb1acff7","time":1588075060311}; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1588072391,1588076777; __mta=219111078.1588072392456.1588075711746.1588076781407.10; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1588076870; mojo-trace-id=18; _lxsdk_s=171c0a65690-38c-554-d1c%7C%7C32',
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}
req = request.Request(url,headers=headers)
result = request.urlopen(req).read().decode('utf-8')
# print(result)
ele = etree.HTML(result)
list1 = ele.xpath('//div[@class="main"]//dl/dd//a[@class="image-link"]/@href')
list0=[]
for i in re.findall('integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>', result):
    p=i[0]+i[1]
    list0.append(p)
# print(list1)
a='https://maoyan.com'
l0=[]
for i in list1:
    b=a+i
    req1=request.Request(b,headers=headers1)
    result1=request.urlopen(req1).read()
    result2 = gzip.decompress(result1)
    result3=result2.decode()
    name=etree.HTML(result3).xpath('//h1[@class="name"]/text()')[0]
    name1=etree.HTML(result3).xpath('//div[@class="ename ellipsis"]/text()')[0]
    fenlei=etree.HTML(result3).xpath('//li[@class="ellipsis"]/a/text()')
    fenleis=''.join(fenlei)
    contry=''.join(etree.HTML(result3).xpath('//li[@class="ellipsis"]/text()')).strip()
    l=[name1,name,fenleis,contry]
    l0.append(l)
print(l0)

















