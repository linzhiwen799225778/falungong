import random
import pymysql
import requests
from lxml import etree
# 存储IP的容器
# 容器，可以存放，可以提取，删除IP，获取IP多少数量，池的容量...
class DB:
    def __init__(self):
        self.conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            passwd="123456",
            db="spider",
            charset="utf8"
        )
        self.cursor = self.conn.cursor()
    # 存放
    def save(self,ip): # ip是传过来的代理
        sql = "insert into ips values(%s)"
        self.cursor.execute(sql,[ip])
        self.conn.commit()
    # 提取所有IP
    def get_all_ip(self):
        sql = "select * from ips"
        self.cursor.execute(sql)
        return self.cursor.fetchall() # 提取所有的ip
    # 删除
    def delete_ip(self,ip):
        sql = "delete from ips where ip=%s" # 删除传过来的IP
        self.cursor.execute(sql,[ip])
        self.conn.commit()
    # 获取数量
    def get_count_ip(self):
        sql = "select * from ips"
        self.cursor.execute(sql)
        return len(self.cursor.fetchall()) # 二维元组长度
    # 提取一条IP
    def get_ip(self):
        sql = "select * from ips"
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0] # 提取所有的ip
# 对池进行操作：获取到IP往池里放，检测IP是否可用，抽样检测，全部检测...
class Pool(): # 唯一我们代码使用的对象
    def __init__(self,yuzhi): # 属性：DB对象，阈值
        self.yuzhi = yuzhi
        self.db = DB()
    def crawl_ip(self):
        # 没到阈值，就爬取
        if self.db.get_count_ip()<self.yuzhi:
            num = 1
            while True:
                url = "https://www.xicidaili.com/nn/{}".format(num)
                print("第{}页".format(num))
                num += 1
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
                }
                res = requests.get(url,headers=headers).text
                ele = etree.HTML(res)
                ips = ele.xpath("//table[@id='ip_list']/tr/td[2]/text()")
                ports = ele.xpath("//table[@id='ip_list']/tr/td[3]/text()")
                types = ele.xpath("//table[@id='ip_list']/tr/td[6]/text()")
                result = zip(ips, ports, types)
                proxy = {}
                for i in result:
                    # print(i)  # i是元组，包含了ip，端口号，类型
                    proxy[i[2]] = i[2]+"://"+i[0] + ":" + i[1]  # 往字典里添加数据
                    # ip如果可用，就保存
                    if self.check_ip(proxy):
                        print("IP可用：{}".format(proxy))
                        self.db.save(str(proxy))
                    proxy = {}  # 没拿一次，清空掉字典
        else:
            print("IP池已满")
    # 检测IP是否可用
    def check_ip(self,ip): # 接收到需要检测的IP
        try:
            target = requests.get("http://www.httpbin.org/ip",proxies=ip).text
            if "39.166.97.63" not in target:
                return True
        except:
            pass
        return False
    # 全部检测
    def check_all_ip(self):
        for ip in self.db.get_all_ip():
            # 不可用的ip，删除
            if not self.check_ip(eval(ip[0])):
                self.db.delete_ip(ip[0])
    # 抽样检测
    def check_many_ip(self,num):
        choice = random.sample(self.db.get_all_ip(),num)
        for ip in choice:
            if not self.check_ip(eval(ip[0])):
                self.db.delete_ip(ip[0])
    # 接口：往出提供IP
    # 获取所有IP
    def get_all_ip(self):
        # 自定义获取所有还是获取一条
        ips = self.db.get_all_ip()
        # 把拿出来的IP从数据库里删掉
        for ip in ips:
            self.db.delete_ip(ip[0])
        return ips
    # 获取一个IP
    def get_ip(self):
        ip = self.db.get_ip()[0] # 一条ip字符串
        # 把拿出来的IP从数据库里删掉
        self.db.delete_ip(ip)
        return eval(ip) # return 字典

pool = Pool(10)
# pool.crawl_ip()
# pool.check_all_ip()
print(pool.get_ip())
