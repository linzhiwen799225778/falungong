import requests
import json
import MySQLdb
conn=MySQLdb.connect(
    port=3306,
    host='127.0.0.1',
    password='123456',
    user='root',
    db='spider',
    charset='utf8',
)
sql4='insert into yi_shi values (%s,%s,%s,%s,%s,%s)'
sql3='insert into yi_sheng values (%s,%s,%s,%s,%s)'
sql2='insert into yi_count values (%s,%s,%s,%s)'

url='https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery34105819522456071067_1589887712686&_=1589887712687'
res=requests.get(url).text
# print(res)
res0=res.split('jQuery34105819522456071067_1589887712686(')[1][0:-1]
res1=json.loads(res0)['data']
res2=json.loads(res1)['areaTree'][0]['children']
res3=json.loads(res1)
print(res3)
confirm_suspect=res3['chinaTotal']['suspect']
confirm_confirm=res3['chinaTotal']['confirm']
confirm_heal=res3['chinaTotal']['heal']
confirm_dead=res3['chinaTotal']['dead']

cursor=conn.cursor()
cursor.execute(sql2,(confirm_confirm,confirm_dead,confirm_heal,confirm_suspect))
conn.commit()
for i in res2:
    sheng=i['name']
    nowConfirm=i['total']['nowConfirm']
    confirm=i['total']['confirm']
    dead=i['total']['dead']
    heal=i['total']['heal']
    shis=i['children']
    cursor.execute(sql3,(sheng,nowConfirm,confirm,dead,heal))
    conn.commit()
    for j in shis:
        shi=j['name']
        nowConfirms=j['total']['nowConfirm']
        confirms=j['total']['confirm']
        deads=j['total']['dead']
        heals=j['total']['heal']
        cursor.execute(sql4,(sheng,shi,nowConfirm,confirm,dead,heal))
        conn.commit()

