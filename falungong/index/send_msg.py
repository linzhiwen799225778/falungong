import django
import requests
import random,string
from index.models import *
import json
import os
django.setup()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "falungong.settings")
class Msg:
    def __init__(self):
        self.url='https://sms.yunpian.com/v2/sms/single_send.json'
    def send_msg(self,phone,code):
        data={
            'apikey':'48525f4edaf0ef945009d1761e3bc676',
            'mobile':phone,
            'text':'【林志文test】您的验证码是{}'.format(code)
        }
        req=requests.post(self.url,data=data)

if __name__ == '__main__':
    pass
    # M=Msg()
    # M.send_msg(17640635281,123456)