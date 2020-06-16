import datetime
import redis
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from index.send_msg import *
from index.models import lunbo_picture
import json
# Create your views here.

myredis=redis.Redis(host='127.0.0.1',port=6379)



# 首页展示
def show_index(request):
    return render(request,'index.html')







# 点击轮播图列表显示
def banner(request):
    return render(request,'banner.html')


# 轮播图显示后加载的表格中的数据
def lunbo_show(request):
    lunbopic=lunbo_picture.objects.all()
    row_num=request.GET.get('rows')
    page=request.GET.get('page')
    allpage=Paginator(lunbopic,row_num)
    lunbopi=allpage.page(page)
    data={
        "page": page,
        "total": allpage.num_pages,  # 总页数
        "records": allpage.count,  # 总条数
        "rows": list(lunbopi)
    }
    def xulie(u):
        if isinstance(u,lunbo_picture):
            return {
                 "id":u.id,
                 "desc":u.desc,
                 "date":u.date,
                 "status":u.status,
                 "pic":str(u.pic)
            }
    res=json.dumps(data,default=xulie)
    return HttpResponse(res)

@csrf_exempt
def option(request):
    '''
    desc: 轮播图2
status: 2
oper: edit
id: 2
    :param request:
    :return:
    '''
    option=request.POST.get('oper')
    if option == 'edit':
        id = request.POST.get('id')
        status = int(request.POST.get('status'))
        desc = request.POST.get('desc')
        obj=lunbo_picture.objects.get(id=id)
        obj.desc=desc
        obj.status=status
        obj.save()
    if option == 'del':
        id = request.POST.get('id')
        student = lunbo_picture.objects.get(id=id)
        student.delete()
    return HttpResponse('1')

@csrf_exempt
def addlunbo(request):
    '''
    title:
    status:
    img: undefined
    :param request:
    :return:
    '''
    title=request.POST.get('title')
    status=request.POST.get('status')
    img=request.FILES.get('img')
    now=datetime.datetime.now()
    lunbo_picture.objects.create(desc=title,date=now,pic=img,status=status)
    return HttpResponse('success')


def login(request):
    return render(request,'login.html')


# 发送验证码
@csrf_exempt
def sendmsg(request):
    phone=request.POST.get('mobile')
    code=str(random.randint(100000,999999))
    print(phone,code)
    # Msg().send_msg(phone=phone,code=code)
    myredis.setex(phone,60,code)
    return HttpResponse('1')

# 验证码验证
@csrf_exempt
def checkmsg(request):
    phone=request.POST.get('phone')
    code=request.POST.get('code')
    if myredis.get(phone):
        codes=str(myredis.get(phone),'utf-8')
    else:codes='o'
    if codes==code:
        return HttpResponse('验证成功')
    else:return HttpResponse('验证失败')


