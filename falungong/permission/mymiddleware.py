import re

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class mymiddlewares(MiddlewareMixin):
    def process_request(self,request):
        url=request.path
        print(url)
        urls=request.session.get('permission_url')
        print(urls)
        baimindan=['/permission/login/','/permission/login_logic/','/admin/.*','/index/sendmsg/']
        for i in baimindan:
            if re.match(i,url):
                print(re.match(i,url))
                return None
        for i in urls:
            if url==i:
                return None
        return HttpResponse('拒绝访问')
