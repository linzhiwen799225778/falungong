import random
import string
import hashlib
from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse

from home.models import *
from yanzhengma.image import ImageCaptcha



def login(request):
    name_cook=request.COOKIES.get('name')
    if name_cook:
        if TUser.objects.filter(username=name_cook):
            ur=reverse('home:index')
        return redirect(ur+'?name='+name_cook)
    return render(request,'login.html')

def login_logic(request):
    name=request.POST.get('name')
    pwd=request.POST.get('pwd')
    capt=request.POST.get('capt')
    cook=request.POST.get('cook')
    captr=request.session.get('logcapt')
    url=request.session.get('url')

    if capt.upper()==captr.upper():
        # req = HttpResponse(reverse('home:index'))
        salt=TUser.objects.filter(username=name)
        if salt:
            salt = TUser.objects.filter(username=name)[0].salt
            pwdadd = pwd + salt
            sha = hashlib.md5()
            sha.update(pwdadd.encode())
            pwdaddmi = sha.hexdigest()
            if TUser.objects.filter(username=name, password=pwdaddmi, salt=salt):
                if TUser.objects.filter(username=name, password=pwdaddmi, salt=salt)[0].is_active:
                    if '?' in url:
                        req = HttpResponse(url + '&name=' + name)
                    else:
                        req = HttpResponse(url + '?name=' + name)
                    if cook:
                        name = req.set_cookie('name', name, max_age=7 * 24 * 3600)
                    return req
                else:
                    return HttpResponse('1')
        else:
            return HttpResponse('0')
    return HttpResponse('0')


def getcapt(request):
    str1=''.join(random.sample(string.ascii_letters+string.digits,4))
    capt=ImageCaptcha().generate(str1)
    request.session['logcapt']=str1
    return HttpResponse(capt,'image/png')