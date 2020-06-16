# -*- coding: utf-8 -*-
import scrapy


class AaSpider(scrapy.Spider):
    name = 'aa'
    # allowed_domains = ['aa.com']
    # start_urls = ['https://www.58.com/zufang/']

    def start_requests(self):
        header = {
                ':authority': 'sh.58.com',
                ': method': 'GET',
                ': path': '/ zufang /',
                ': scheme': 'https',
                'accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9',
                'accept - encoding': 'gzip, deflate, br',
                'accept - language': 'zh - CN, zh;q = 0.9',
                'cache - control': 'max - age = 0',
                'referer': 'https: // www.58.com / zufang /',
                'sec - fetch - dest': 'document',
                'sec - fetch - mode': 'navigate',
                'sec - fetch - site': 'same - site',
                'sec - fetch - user': '?1',
                'upgrade - insecure - requests': '1',
                'user - agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 80.0.3987.132Safari / 537.36',
                }
        url='https://sh.58.com/zufang/'
        yield scrapy.Request(url=url,headers=header)
    def parse(self, response):
        res=response.xpath('//ul[@class="house-list"]/li[@class="house-cell"]//span[@class="listjjr"]/text()').getall()
        for i in res:
            print(i.strip())
