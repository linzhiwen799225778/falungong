import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
import redis
# Create your views here.
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from index.models import *
from context.models import *
from permission.models import *
from zhuanji.models import *
from user.models import *

myredis=redis.Redis(host='127.0.0.1',port=6379,)
import random

def get(request):
    """
    返回前台系统所需的首页数据
    :param request:uid
    :return:
    """
    user_id = request.GET.get("id")
    print(user_id)
    if not user_id:
        result = {"status": 500, "message": "用户不存在"}
        return JsonResponse(result)

    # TODO 查询首页所需的数据 并以json的形式返回到前台
    # 轮播图获取
    emp_set = lunbo_picture.objects.all()
    def my_default(u):
        if isinstance(u, lunbo_picture):
            return {
                "id": u.pk,
                "desc": u.desc,
                "date": u.date,
                "status": u.status,
                "pic": str(u.pic)
            }

    json_dumps = json.dumps(list(emp_set), default=my_default)
    # 专辑
    album = zhuanjis.objects.all()
    def myDefault(u):
        if isinstance(u, zhuanjis):
            return {
                "album_id": u.id,
                "id": u.id,
                "title": u.title,
            }
    data = json.dumps(list(album), default=myDefault)
    # 文章
    article = Context.objects.all()
    def myDefault(u):
        if isinstance(u, Context):
            return {'id': u.id,
                    'content': u.title,
                    'title': u.title,
                    'status': u.status,
                    'fenlei': u.fenlei,
                    'neirong': u.neirong,
                    }

    dates = json.dumps(list(article), default=myDefault)
    result = {
        "status": 200,
        "message": "success",
        "header": json_dumps,
        "album": data,
        "article": dates,
    }
    return HttpResponse(json_dumps)




def zhuanji(request):
    zhuanji_id = request.GET.get("id")
    if not zhuanji_id:
        result = {"status": 500, "message": "用户不存在"}
        return JsonResponse(result)

    album =zhangjie.objects.filter(id=zhuanji_id)
    def myDefault(u):
        if isinstance(u, zhangjie):
            return {
                "album_id": u.zhangjie_name,
                "size": u.zhangjie_size,
                "url": u.url,
                "id": u.id,
            }

    data = json.dumps(list(album), default=myDefault)
    result = {
        "status": 200,
        "message": "success",
        "album": data,
    }
    return JsonResponse(data)





@csrf_exempt
def zhuce(request):
    """
    前台app用户注册逻辑
    :param request:
    :return:
    """
    phone = request.POST.get("phone")
    pwd = request.POST.get("password")
    print(phone, pwd)
    # TODO 获取用户信息完成注册  注册完成后将用户信息返回到前台
    if User.objects.filter(username=phone):
        res={
            "errno": "-200",
            "error_msg": "该手机号已经存在",
        }
        return JsonResponse(res)

    user_id = User.objects.create(username=phone,password=pwd).id
    print(user_id,phone,pwd)
    res={
        "status": 200,
        "phone":phone,
        "password":pwd,
        "user_id":user_id,
    }
    return JsonResponse(res)
    # return HttpResponse("OK")


@csrf_exempt
def xiugai(request):
    id = request.POST.get("id")
    phone = request.POST.get("phone")
    password = request.POST.get("password")
    if User.objects.filter(id=id):
        user = User.objects.get(id=id)
        user.username = phone
        user.password = password
        user.save()
        res = {
            "status": 200,
            "phone": phone,
            "password": password,
            "user_id": id,
        }
        return JsonResponse(res)
    res = {
        "errno": "-200",
        "error_msg": "该用户不存在",
    }
    return JsonResponse(res)
