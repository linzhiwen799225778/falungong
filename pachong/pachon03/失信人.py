import requests
import json
from headers import get_headers
import MySQLdb
url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
    "Referer": "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA&fenlei=256&rsv_pq=892ce10600149fc6&rsv_t=bba6O39OhgTmZAKzgm75XEINeiLjv88%2F9bIIP7iymZRtLxT%2BPmOz4ds0%2BbE&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=11&rsv_sug1=7&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=1681&rsv_sug4=2950"

}
# get_headers(headers)
iname = "赵谦孙俪周五正往冯陈楚为和律师张发生发342vsfaa"

str1 = """
resource_id: 6899
query: 失信被执行人名单
cardNum: 
iname: 赵
areaName: 
pn: 10
from_mid: 1
ie: utf-8
oe: utf-8
format: json
cb: jQuery110208174968884452374_1588210302615
"""
connect=MySQLdb.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    passwd = "123456",
    db = "spider",
    charset="utf8"
)
curcor=connect.cursor()
params = get_headers(str1)
def  save_duandian(name,page):
    sql='update duandian set name=%s ,page=%s'
    curcor.execute(sql,[name,page])
    connect.commit()
for name in iname:
    sum_num = 0
    params["pn"] = str(0)
    while sum_num<30: #出现30次相同的案号，停止循环，进入下一次for循环
        params["iname"] = name
        print(iname.index(name),params["pn"])
        res = requests.get(url,headers=headers,params=params).content.decode("utf-8")
        new_res = json.loads(res[46:-2])
        for i in new_res['data'][0]['disp_data']:
            try:
                print(i['gistId']) # 案号作为主键，同样的案号插入会报错
                print(i['courtName'])
            except:
                sum_num += 1
        params["pn"] = str(eval(params["pn"]) + 10)
        save_duandian(name,params["pn"])