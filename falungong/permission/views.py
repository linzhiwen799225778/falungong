from django.http import HttpResponse
from django.shortcuts import render, redirect
import redis
from django.views.decorators.csrf import csrf_exempt

myredis=redis.Redis(host='127.0.0.1',port=6379)
# Create your views here.
from permission.models import User
def login(request):
    return render(request,'login.html')
@csrf_exempt
def login_logic(request):
    name=request.POST.get('name')
    password=request.POST.get('password')
    phone=request.POST.get('phone')
    code=request.POST.get('code')
    if myredis.get(phone):
        codes=str(myredis.get(phone),'utf-8')
    else:codes='o'
    if codes!=code:
        return HttpResponse('验证码验证失败')
    user=User.objects.filter(username=name,password=password).first()
    if not user:
        return HttpResponse('用户不存在')
    permission=user.roles.all().values('permission__url',
                                       'permission__parentid',
                                       'permission__ismenu',
                                       'permission__title',
                                       ).distinct()
    menu=[]
    for i in permission:
        if i['permission__ismenu']:
            dic={
                'parentid':i['permission__parentid'],
                 'title':i['permission__title'],
                'url': i['permission__url'],
                 }
            menu.append(dic)
    l=[i['permission__url'] for i in permission]
    request.session['permission_url']=l
    request.session['menu']=menu
    return HttpResponse('success')