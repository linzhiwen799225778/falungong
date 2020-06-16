import json

from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from user.models import *
# Create your views here.
# 显示用户列表
def userlist(request):
    return render(request,'userlist.html')


# 加载用户数据
def loaduser(request):
    users = User.objects.all()
    row_num = request.GET.get('rows')
    page = request.GET.get('page')
    allpage = Paginator(users, row_num)
    userpage = allpage.page(page)
    data = {
        "page": page,
        "total": allpage.num_pages,  # 总页数
        "records": allpage.count,  # 总条数
        "rows": list(userpage)
    }

    def xulie(u):
        if isinstance(u, User):
            print(u.headpic)
            return {
                "id": u.id,
                "name": u.name,
                "phone": u.phone,
                "status": u.status,
                "city": u.city,
                "sex":u.sex,
                "data":u.headpic,
            }

    res = json.dumps(data, default=xulie)
    return HttpResponse(res)

@csrf_exempt
def option(request):
    option=request.POST.get('oper')
    if option == 'edit':
        id = request.POST.get('id')
        status = request.POST.get('status')
        obj=User.objects.get(id=id)
        obj.status=status
        obj.save()
    return HttpResponse('修改成功')

# 缓存用户请求的访问记录
@cache_page(timeout=600,key_prefix="cacheRedis3")
def get_map(request):
    a=User.objects.values('city').annotate(Count('city'))
    b=[]
    for i in a:
        c={}
        c['name']=i['city'][0:2]
        c['value']=i['city__count']
        b.append(c)
    return JsonResponse(b,safe=False)