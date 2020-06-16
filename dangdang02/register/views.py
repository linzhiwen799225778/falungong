import random,string
import hashlib,uuid
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.contrib.auth import settings
from django.core.mail import send_mail
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from yanzhengma.image import ImageCaptcha
from home.models import  *


def registe(request):
    return render(request,'register.html')

def capt(request):
    str1=''.join(random.sample(string.ascii_letters+string.digits,4))
    img=ImageCaptcha().generate(str1)
    request.session['rcapt']=str1
    return HttpResponse(img,'image/png')

def checkname(request):
    name=request.POST.get('name')
    if TUser.objects.filter(username=name):
        return  HttpResponse(0)
    return HttpResponse(1)

def regidterok(request):
    salt=str(uuid.uuid4())
    name=request.POST.get('txt_username')
    pwd=request.POST.get('txt_password')+salt
    sha=hashlib.md5()
    sha.update(pwd.encode())
    pwd_addmi=sha.hexdigest()
    TUser.objects.create(username=name,password=pwd_addmi,salt=salt)
    userid=TUser.objects.filter(username=name)[0].id
    ser=Serializer(settings.SECRET_KEY,expires_in=120)
    token=ser.dumps({'id':userid})
    token=token.decode('utf-8')
    send_mail('激活用户', 'http://127.0.0.1:8000/register/email/?token='+token, '799225778@qq.com', [name], fail_silently=False)
    return render(request,'register ok.html',{'name':name})

def captcheck(request):
    captr=request.session.get('rcapt')
    capt=request.GET.get('code')
    if capt.upper()==captr.upper():
        return HttpResponse('1')
    return HttpResponse('0')


def regokjump(request):
    name=request.GET.get('name')
    url=request.session.get('url')
    if '?' in url:
        url=request.session.get('url')+'&name='+name
    else:url=request.session.get('url')+'?name='+name
    return redirect(url)


def email(request):
    token=request.GET.get('token')
    ser=Serializer(settings.SECRET_KEY,expires_in=120)
    result=ser.loads(token)
    id=result.get('id')
    tuser=TUser.objects.filter(id=id)[0]
    tuser.is_active=True
    tuser.save()
    return HttpResponse('激活成功')