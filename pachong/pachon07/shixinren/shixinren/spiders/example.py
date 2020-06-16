# -*- coding: utf-8 -*-
from urllib.parse import urlencode

import scrapy
import requests
import json
from urllib import request

class ExampleSpider(scrapy.Spider):
    name = 'shixinren'
    # allowed_domains = ['example.com']
    # start_urls = ['https://sp0.baidu.com']
    def start_requests(self):
        url='https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Referer': 'https://www.baidu.com/s?ie=utf-8&tn=02003390_21_hao_pg&wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA',
        }
        num = 0
        for i in range(10):
            pn = str(num)
            params = {
                'resource_id': '6899',
                'query': '失信被执行人名单',
                'cardNum': '',
                'iname': '飞',
                'areaName': '',
                'from_mid': '1',
                'ie': 'utf-8',
                'pn': pn,
                'oe': 'utf-8',
                'format': 'json',
                't': '1588939871111',
                'cb': 'jQuery110207699634863779086_1588939831840',
                '_': '1588939831843',
            }
            num += 10
            new_params=urlencode(params)
            new_url=url+new_params
            yield scrapy.Request(new_url,headers=header,callback=self.parse)
    def parse(self, response):
        res=response.text
        # res=response.text
        peoples=json.loads(res[46:-2])['data'][0]['disp_data']
        for i in peoples:
            b = i['iname']
            print(b)