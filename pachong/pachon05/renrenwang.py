from pachon03.myheaders import get_cookies,get_headers
import requests
import MySQLdb
from lxml import etree
from pachon05.chaojiying import code
num=1
# url='http://www.renren.com/880151247/profile'
str2="""
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Connection: keep-alive
Host: www.renren.com
Referer: http://www.renren.com/974381051
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36
"""
header=get_headers(str2)
connect=MySQLdb.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="123456",
    db="spider",
    charset="utf8"
)
cursor=connect.cursor()
# str1='anonymid=k9v4xeck-6qoec6; depovince=GW; _r01_=1; JSESSIONID=abcRa7NZGi4rf84vltPhx; ick_login=3cd766f2-3d20-47e7-9a34-a44dd1cba9ca; taihe_bi_sdk_uid=95f5dafa8ffa9a7458fde754af25b6d4; taihe_bi_sdk_session=92371c545b0f984b64872770a35a1538; t=bfef3ee5f60093086981a1fbbd5517651; societyguester=bfef3ee5f60093086981a1fbbd5517651; id=974381051; xnsid=16b2b283; ver=7.0; loginfrom=null; jebecookies=869ba5cf-f740-4af6-8219-fb8f4e2ca057|||||; jebe_key=0ac01e34-e5e0-4a14-8be6-d1bf4c549e44%7Cbd717e3fcc2b16ab86178755999c50f4%7C1588757113418%7C1%7C1588757113920; jebe_key=0ac01e34-e5e0-4a14-8be6-d1bf4c549e44%7Cbd717e3fcc2b16ab86178755999c50f4%7C1588757113418%7C1%7C1588757113926; wp_fold=0'
# cookie=get_cookies(str1)
cookie={'t':'bfef3ee5f60093086981a1fbbd5517651'}
# res=requests.get(url,headers=header,cookies=cookie).text
# ele=etree.HTML(res)
# name=ele.xpath('//title/text()')[0]
# urls=ele.xpath('//div[@id="footprint-box"]//ul/li/a/@namecard')
#存url
def save_url(urls):
    for i in urls:
        try:
            sql='insert into renurls values(%s,%s)'
            cursor.execute(sql,[i,'0'])
            connect.commit()
        # url = 'http://www.renren.com/'+str(i)+'/profile'
        # res = requests.get(url, headers=header, cookies=cookie).text
        # ele = etree.HTML(res)
        # name = ele.xpath('//title/text()')[0]
        except:pass
#存名字
def save_name(name):
    sql='insert into rendata values(%s)'
    cursor.execute(sql,[name])
    connect.commit()
#改状态
def change_statu(url):
    sql='update renurls set state = %s where renurl=%s'
    cursor.execute(sql,['1',url])
    connect.commit()
# 获取url
def get_url():
    sql='select renurl from renurls where state=%s'
    cursor.execute(sql,['0'])
    url=cursor.fetchone()[0]
    detail_url(url)

def detail_url(url):
    detail_url='http://www.renren.com/'+str(url)+'/profile'
    res=requests.get(detail_url,headers=header,cookies=cookie).text
    change_statu(url)
    ele=etree.HTML(res)
    try: # 处理被封禁的用户
        username = ele.xpath("//title/text()")[0]
        save_name(username)
    except:
        pass
    print(username)
    if username == '人人网 - 验证码':
        yanzhengurl = etree.HTML(res).xpath('//div[@class="optional"]//img/@src')[0]
        res = requests.get(yanzhengurl,cookies=cookie).content
        print(res)
        check_code(res)
    else:
        urls = ele.xpath('//div[@id="footprint-box"]//ul/li/a/@namecard')
        print(urls)
        save_url(urls)
def check_code(img):
    cade=code(img)
    print(cade)
    data={
        'id': '973987717',
        'icode': cade,
        'submit': '继续浏览',
        'requestToken': '563997865',
        'rtk': 'ed5eeb03',
    }
    url='http://www.renren.com/validateuser.do'
    requests.post(url,data=data,cookies=cookie)
while 1:
    get_url()













