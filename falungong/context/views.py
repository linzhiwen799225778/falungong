import json
import os

from django.core.paginator import Paginator
from django.http import  HttpResponse,JsonResponse
from django.shortcuts import render
# Create your views here.
# 显示文章列表
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt
from context.models import *

def show_context(request):
    return render(request,'centextlist.html')

# 上传图片
@xframe_options_sameorigin
@csrf_exempt
def uppic(request):
    image = request.FILES.get("imgFile")
    print(image)
    if image:
        # http://127.0.0.1:8000/static/img/000.jpg
        img_url = request.scheme + "://" + request.get_host() + "/static/img/up_pic/" + str(image)
        result = {"error": 0, "url": img_url}
        Pic.objects.create(img=image)
        print(result)
    else:
        result = {"error": 500, "url": "图片上传失败"}
    print(result)
    return JsonResponse(result,safe=False, content_type="application/json")

# 返回上传历史
def pic_history(request):
    '''
    :param request:
    :return:
    '''
    url=request.scheme+'://'+request.get_host()+'/'
    print(url)
    pics=Pic.objects.all()
    l=[]
    for i in list(pics):
        path,img_png=os.path.splitext(i.img.url)
        l.append(
            {"is_dir": False,
             "has_file": False,
             "filesize": i.img.size,
             "dir_path": "",
             "is_photo": True,
             "filetype": img_png,
             "filename": i.img.name,
             "datetime": "2018-06-06 00:36:39"},
        )
        print(i.img.size,i.img.name)
    data={
        "moveup_dir_path": "",
        "current_dir_path": "",
        "current_url": url,  # 图片空间的路径
        "total_count": len(pics),  # 图片的总数
        # 所有图片的属性
        "file_list": l
    }
    return HttpResponse(json.dumps(data), content_type="application/json")



# 获取文章内容
def get_context(request):
    context=Context.objects.all()
    rows=request.GET.get('rows')
    page=request.GET.get('page')
    paginator=Paginator(context,rows)
    contextlist=paginator.page(page)
    data = {
        "page": page,
        "total":paginator.num_pages,  # 总页数
        "records": paginator.count,  # 总条数
        "rows": list(contextlist)
    }
    def json_context(u):
        if isinstance(u,Context):
            print(u.fenlei,84)
            return {
                'id':u.id,
                'status':u.status,
                'title':u.title,
                'neirong':u.neirong,
                'fenlei':u.fenlei,
            }
    res=json.dumps(data,default=json_context)


    return HttpResponse(res)

@csrf_exempt
def option_context(request):

    id=request.POST.get('id')
    option=request.POST.get('oper')
    if option=='edit':
        status = request.POST.get('status')
        print(status,type(status))
        context=Context.objects.get(id=id)
        context.status=status
        context.save()
    if option == 'del':
        Context.objects.get(id=id).delete()
    return HttpResponse('11')


def save_context(request):
    title=request.GET.get('title')
    leixing=request.GET.get('leixing')
    context=request.GET.get('context')
    print(title,leixing,context)
    Context.objects.create(title=title,fenlei=leixing,neirong=context)
    return HttpResponse('保存成功！')
