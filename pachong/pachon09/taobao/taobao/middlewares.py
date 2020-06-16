# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from pachon03 import myheaders

class TaobaoSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TaobaoDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        cook = 'miid=1774419420880723551; _m_h5_tk=9700ab8abefef4358092d7f28b4ed613_1589205963321; _m_h5_tk_enc=31403f07ed04312de5d9ddbb7584c8b7; cna=b3HKFqfx+gcCAXUsEJj3pQhN; _samesite_flag_=true; cookie2=195a9e27d66dd7ca86409576f3366249; t=8a6223de32b53271635ecf7e3f1aeea9; _tb_token_=513030e658b3; sgcookie=EjXrH%2BYFLlqdYs7ENBPt0; unb=2291398965; uc3=vt3=F8dBxGXL%2FZTDTP28Y1g%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D&id2=UUpobRCJNDRleg%3D%3D&nk2=oiRCVACqWFmFckhKqnQ%3D; csg=90c17179; lgc=%5Cu6797%5Cu5E08%5Cu5085%5Cu5403%5Cu5EB7%5Cu5E08%5Cu5085; cookie17=UUpobRCJNDRleg%3D%3D; dnk=%5Cu6797%5Cu5E08%5Cu5085%5Cu5403%5Cu5EB7%5Cu5E08%5Cu5085; skt=1c4a5d844b9ef419; existShop=MTU4OTE5ODQzOA%3D%3D; uc4=nk4=0%40oCaauYTwZaBvsDyOysBnRYwTVAMc8W79Bw%3D%3D&id4=0%40U2giQHnLfGCBAPXxpEZ3o753G98r; tracknick=%5Cu6797%5Cu5E08%5Cu5085%5Cu5403%5Cu5EB7%5Cu5E08%5Cu5085; _cc_=URm48syIZQ%3D%3D; _l_g_=Ug%3D%3D; sg=%E5%82%855a; _nk_=%5Cu6797%5Cu5E08%5Cu5085%5Cu5403%5Cu5EB7%5Cu5E08%5Cu5085; cookie1=UoSJK%2BlLsL2T1P3i2Xatxmgn%2F3xodGzy%2F2Un3AuzhtI%3D; tfstk=cIo1B9bIC1fsIAmNYj9UuBRV8_EVaasQKMVEC2jmWPbeitD_9smf47T0DR1CvzeC.; mt=ci=2_1; v=0; thw=cn; uc1=cookie14=UoTUM2FuXUnhGg%3D%3D&cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie21=WqG3DMC9Fb5mPLIQo9kR&pas=0&existShop=false; enc=xgLmTIEozNLNTjP6ZyCK17FgEofQiy%2Bzv1AGdHWJO%2Fsyrr9E7APeKUBnZY4PCdCa8TNX57gWLDq11SFc8NsLNQ%3D%3D; JSESSIONID=5A8A9B8580DCC74ADBC529A07348F4EC; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; hng=CN%7Czh-CN%7CCNY%7C156; l=eBT6KTSlQ3ym-GMEBOfwPurza77OSIRAguPzaNbMiTfP9Mfp5yPcWZb6SRL9C3GVh6V6R354uljBBeYBqIv4n5U62j-la_kmn; isg=BNTUgqh9dj6olOJyIOI4wZDZpRJGLfgXxaHE0W61YN_iWXSjlj3Ip4rbXVFBoTBv'
        cookies = myheaders.get_cookies(cook)
        request.cookies.update(cookies)
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
