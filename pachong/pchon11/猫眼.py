# import requests
# from fontTools.ttLib import TTFont
# # url='https://vfile.meituan.net/colorstone/0fe21edea57e467357478903e4eb2a9d2272.woff'
# #
# # res=requests.get(url).content
# # with open('2.woff','w') as w:
# #     w.write(res)
# T=TTFont('11.woff')
# T.saveXML('11.xml')

import requests
from lxml import etree
import gzip
url='https://maoyan.com/board/4?offset=0'
header={
    'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
header0={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'__mta=219111078.1588072392456.1589597394582.1589598159181.19; uuid_n_v=v1; uuid=3E27D9A0894111EAA1C98B1F174282C890E7C17DC1EF4824A8E836D01CA841A7; _lxsdk_cuid=171c07da3777f-0e736f17c06bc6-3a65420e-100200-171c07da378c8; _lxsdk=3E27D9A0894111EAA1C98B1F174282C890E7C17DC1EF4824A8E836D01CA841A7; t_lxid=171c07da52a1b-01f3ccf626f778-3a65420e-100200-171c07da52bc8-tid; mojo-uuid=77c61233368b7b1ad4e30a0aae285262; _csrf=e7d6c7ff7b80b57a78341cac51d0619e193962c4eee60cd65699c6b95f053fce; mojo-session-id={"id":"d0b07738f088227d0dc84c5a810863fd","time":1589597249387}; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic%26utm_term%3D%25E7%258C%25AB%25E7%259C%25BC%25E7%2594%25B5%25E5%25BD%25B1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1588083704,1588084099,1589544973,1589597251; __mta=219111078.1588072392456.1589597423629.1589597425591.29; mojo-trace-id=27; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1589598157; _lxsdk_s=1721b612011-7fb-fce-c2f%7C%7C42',
'Host':'maoyan.com',
'Upgrade-Insecure-Requests':'1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
res=requests.get(url=url,headers=header).text
# print(res)
ele=etree.HTML(res)
detial_url=ele.xpath('//*[@id="app"]/div/div/div[1]/dl/dd//a[1]/@href')
for i in detial_url:
    new_url='https://maoyan.com/'+i
    print(new_url)
    res0=requests.get(url=new_url,headers=header0).content
    print(res0)
    res1=gzip.decompress(res0)
    print(res1)
    # ele=etree.HTML(res0)
    # name=ele.xpath('/html/body/div[3]/div/div[2]/div[1]/h1')
    # print(name)
    break








