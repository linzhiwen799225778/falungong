# -*- coding: utf-8 -*-
import scrapy
from ..items import JobItem

from scrapy_redis.spiders import RedisSpider
class ExampleSpider(scrapy.Spider):
    name = 'JobSpider'
    # redis_key = 'hehe'
    # allowed_domains = ['example.com']
    def start_requests(self):
        pagenum=1
        while 1:
            url = "https://search.51job.com/list/010000,000000,0000,00,9,99,%25E9%2594%2580%25E5%2594%25AE,2," + str(
                pagenum) + ".html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="
            print("开始抓取第%s页" % pagenum)
            pagenum+=1
            yield  scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        list1 = response.xpath('//div[@class="el"]/p/span/a/@href').getall()
        for pageurl in list1:
            yield scrapy.Request(pageurl,callback=self.parsel)

    def parsel(self,res):
        job_name = res.xpath('//h1/text()').getall()[0]  # 工作名称字符串
        salary = res.xpath('//div[@class="cn"]/strong/text()').getall()
        if not salary:
            salary =['面议']
        company_name = res.xpath('//p[@class="cname"]/a/text()').getall()[0]
        experience=str(res.xpath('//p[@class="msg ltype"]/text()').getall())
        item=JobItem()
        item['name']=job_name
        item['price']=salary[0]
        # item['company_name']=company_name
        # item['experience']=experience
        yield item
        print(job_name,salary[0])
