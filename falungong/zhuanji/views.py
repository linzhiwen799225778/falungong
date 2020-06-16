import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from zhuanji.models import *
# Create your views here.

# 显示专辑列表
def show_zhuanji(request):
    return render(request,'zhuanji.html')


# 获取专辑数据
def get_zhuanji(request):
    list_zhuanji=zhuanjis.objects.all()
    row_num = request.GET.get('rows')
    page = request.GET.get('page')
    allpage = Paginator(list_zhuanji, row_num)
    userpage = allpage.page(page)
    data = {
        "page": page,
        "total": allpage.num_pages,  # 总页数
        "records": allpage.count,  # 总条数
        "rows": list(userpage)
    }

    def xulie(u):
        if isinstance(u, zhuanjis):
            print(u.pic)
            return {
                "id": u.id,
                "title": u.title,
                "score": u.score,
                "statue": u.statue,
                "author": u.author,
                "boyin": u.boyin,
                "zhangjie": u.zhangjieshu,
                "pic": u.pic,
                "jianjie": u.jianjie,
            }

    res = json.dumps(data, default=xulie)
    return HttpResponse(res)



# 操作专辑
@csrf_exempt
def option_zhuanji(request):
    '''
title: 青花瓷
score: 9
author: 周杰伦
boyin: 林志文
jianjie: 非常的好听
statue: 1
oper: edit
id: 1
    :param request:
    :return:
    '''
    option=request.POST.get('oper')
    if option=='edit':
        id = request.POST.get('id')
        zj=zhuanjis.objects.filter(id=id).first()
        title = request.POST.get('title')
        score = request.POST.get('score')
        author = request.POST.get('author')
        boyin = request.POST.get('boyin')
        jianjie = request.POST.get('jianjie')
        statue = request.POST.get('statue')
        zj.title=title
        zj.score=score
        zj.author=author
        zj.boyin=boyin
        zj.jianjie=jianjie
        zj.statue=statue
        zj.save()
    if option == 'del':
        id = request.POST.get('id')
        zj = zhuanjis.objects.filter(id=id).first()
        zj.delete()
    return HttpResponse('成功')



# 获取章节数据
def get_zhangjie(request):
    list_zhangjie=zhangjie.objects.all()
    row_num = request.GET.get('rows')
    page = request.GET.get('page')
    allpage = Paginator(list_zhangjie, row_num)
    userpage = allpage.page(page)
    data = {
        "page": page,
        "total": allpage.num_pages,  # 总页数
        "records": allpage.count,  # 总条数
        "rows": list(userpage)
    }

    def xulie(u):
        if isinstance(u, zhangjie):
            print(u.url)
            return {
                "id": u.id,
                "zhangjie": u.zhangjie_name,
                "zhangjie_size": u.zhangjie_size,
                "url": str(u.url),
            }

    res = json.dumps(data, default=xulie)
    return HttpResponse(res)

# 删除章节
@csrf_exempt
def option_zhangjie(request):
    option=request.POST.get('oper')
    if option=='del':
        id=request.POST.get('id')
        zhangjie.objects.filter(id=id)[0].delete()
    return HttpResponse('操作成功')

@csrf_exempt
def add_zhangjie(request):
    yinyue=request.FILES.get('yinyue')
    title=request.POST.get('title')
    statue=request.POST.get('status')
    id=request.POST.get('id')
    zhuanji=zhuanjis.objects.get(id=id)
    zhangjie.objects.create(zhangjie_name=title,zhangjie_size='5M',url=yinyue,zj_id=zhuanji)
    return HttpResponse(11)