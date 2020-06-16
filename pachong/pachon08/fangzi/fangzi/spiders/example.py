# -*- coding: utf-8 -*-
import scrapy
import re
from pachon03 import myheaders
from pachon09.taobao.taobao.items import TaobaoItem
class ExampleSpider(scrapy.Spider):
    name = 'taobao'
    # allowed_domains = ['example.com']
    # start_urls = ['http://example.com/']
    def start_requests(self):
        a = 0
        header = {
            'authority': 's.taobao.com',
            'method': 'GET',
            'path': '/search?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'referer': 'https://www.taobao.com/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        }
        cook = 'miid=1774419420880723551; _m_h5_tk=9700ab8abefef4358092d7f28b4ed613_1589205963321; _m_h5_tk_enc=31403f07ed04312de5d9ddbb7584c8b7; cna=b3HKFqfx+gcCAXUsEJj3pQhN; _samesite_flag_=true; cookie2=195a9e27d66dd7ca86409576f3366249; t=8a6223de32b53271635ecf7e3f1aeea9; _tb_token_=513030e658b3; sgcookie=EjXrH%2BYFLlqdYs7ENBPt0; unb=2291398965; uc3=vt3=F8dBxGXL%2FZTDTP28Y1g%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&id2=UUpobRCJNDRleg%3D%3D&nk2=oiRCVACqWFmFckhKqnQ%3D; csg=90c17179; lgc=%5Cu6797%5Cu5E08%5Cu5085%5Cu5403%5Cu5EB7%5Cu5E08%5Cu5085; cookie17=UUpobRCJNDRleg%3D%3D; dnk=%5Cu6797%5Cu5E08%5Cu5085%5Cu5403%5Cu5EB7%5Cu5E08%5Cu5085; skt=1c4a5d844b9ef419; existShop=MTU4OTE5ODQzOA%3D%3D; uc4=nk4=0%40oCaauYTwZaBvsDyOysBnRYwTVAMc8W79Bw%3D%3D&id4=0%40U2giQHnLfGCBAPXxpEZ3o753G98r; tracknick=%5Cu6797%5Cu5E08%5Cu5085%5Cu5403%5Cu5EB7%5Cu5E08%5Cu5085; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%82%855a; _nk_=%5Cu6797%5Cu5E08%5Cu5085%5Cu5403%5Cu5EB7%5Cu5E08%5Cu5085; cookie1=UoSJK%2BlLsL2T1P3i2Xatxmgn%2F3xodGzy%2F2Un3AuzhtI%3D; tfstk=cIo1B9bIC1fsIAmNYj9UuBRV8_EVaasQKMVEC2jmWPbeitD_9smf47T0DR1CvzeC.; mt=ci=2_1; v=0; thw=cn; uc1=cookie14=UoTUM2FuXUnhGg%3D%3D&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie21=WqG3DMC9Fb5mPLIQo9kR&pas=0&existShop=false; enc=xgLmTIEozNLNTjP6ZyCK17FgEofQiy%2Bzv1AGdHWJO%2Fsyrr9E7APeKUBnZY4PCdCa8TNX57gWLDq11SFc8NsLNQ%3D%3D; JSESSIONID=5A8A9B8580DCC74ADBC529A07348F4EC; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; l=eBT6KTSlQ3ym-GMEBOfwPurza77OSIRAguPzaNbMiTfP9Mfp5yPcWZb6SRL9C3GVh6V6R354uljBBeYBqIv4n5U62j-la_kmn; isg=BNTUgqh9dj6olOJyIOI4wZDZpRJGLfgXxaHE0W61YN_iWXSjlj3Ip4rbXVFBoTBv'
        cookies = myheaders.get_cookies(cook)
        for i in range(10):
            url = 'https://s.taobao.com/search?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s={}'.format(a)
            a += 44
            yield scrapy.Request(url=url,headers=header)
    def parse(self, response):
        res = response.text
        print(res)
        r = re.findall('g_page_config\s=\s(.*);', res)[0]
        # print(json.loads(r))
        a = re.findall('raw_title":"(.*?)",', r)
        b = re.findall('view_price":"(.*?)",', r)
        print(a,b)
        item=TaobaoItem()
        item['name']=a
        item['price']=b
        yield item

