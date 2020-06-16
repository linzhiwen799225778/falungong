from urllib import request
# url='https://search.51job.com/list/130800,000000,0000,00,9,99,%2B,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
# res=request.urlopen(url).read().decode('gbk')
# 存入到本地
# with open('51job.html','a',encoding='utf-8') as w:
#     w.write(res)
# 存入到数据库
import MySQLdb
conn=MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    charset='utf8',
    db='cra'
)
cursor=conn.cursor()
num=1
while 1:
    url='https://search.51job.com/list/130800,000000,0000,00,9,99,%2B,2,'+str(num)+'.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    num+=1
    res=request.urlopen(url).read().decode('gbk')
    from lxml import etree
    eles=etree.HTML(res)
    list1=eles.xpath('//div[@class="el"]/p[@class="t1 "]/span/a/@href')
    print(list1)
    for i in list1:
        try:
            res1=request.urlopen(i).read().decode('gbk')
            ele=etree.HTML(res1)
            company=ele.xpath('//div[@class="in"]/div[@class="cn"]//a[@class="catn"]/text()')[0]
            jobname=ele.xpath('//div[@class="tHeader tHjob"]//h1/text()')[0]
            salary=ele.xpath('//div[@class="tHeader tHjob"]//strong/text()')[0]
            xueli=ele.xpath('//div[@class="tHeader tHjob"]//p[@class="msg ltype"]/text()')[2]
            worktime=ele.xpath('//div[@class="tHeader tHjob"]//p[@class="msg ltype"]/text()')[1]
            s=cursor.execute('insert into job values (%s,%s,%s,%s,%s)',[company,jobname,salary,xueli,worktime])
            conn.commit()
        except:
            pass
cursor.close()
conn.close()





