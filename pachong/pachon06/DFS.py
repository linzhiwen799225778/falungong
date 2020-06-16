import requests
from lxml import etree

class Dfs:
    def __init__(self):
        self.dfs=[]
        self.crawled=[]
    def save(self,url):
        if url not in self.crawled:
            self.dfs.append(url)
    def get(self):
        url=self.dfs.pop()
        self.crawled.append(url)
        return url
class Crawler:
    def __init__(self):
        self.dfs=Dfs()
    def crawler(self):
        url='http://www.baidu.com'
        self.dfs.save(url)
        while 1 :
            newurl = self.dfs.get()
            try:
                res=requests.get(newurl).content.decode()
                ele=etree.HTML(res)
                urls=ele.xpath('//a/@href')
                title=ele.xpath('//title/text()')
                if self.checkurl(newurl):
                    print(title)
                    print(newurl)
                    for i in urls:
                        self.dfs.save(i)
            except:
                print('url错误',newurl)
    def checkurl(self,url):
        if ('http://ir.baidu.com' in url) or ('http://home.baidu.com/media_resource/' in url):
            return False
        return True
dc=Crawler()
dc.crawler()







