import random
import re
import string
from itertools import chain

from django.http import JsonResponse

from home.car_book import *
from django.core.paginator import Paginator
from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse

from home.models import *
# Create your views here.
def index(request):
    request.session['url'] = request.get_full_path()
    name=request.GET.get('name')
    classa=TSorted.objects.all()
    books=TBook.objects.order_by('shelves_date')[0:8]
    books1=TBook.objects.order_by('shelves_date').order_by('sales')[0:5]
    books2=TBook.objects.order_by('shelves_date').order_by('sales')[0:10]
    if name:
        return render(request,'index.html',{'class':classa,'book':books,'book1':books1,
                                        'book2':books2,'name':name,})
    return render(request, 'index.html', {'class': classa, 'book': books, 'book1': books1,
                                          'book2': books2})

def book_detial(request):
    request.session['url'] = request.get_full_path()
    bookq=request.GET.get('bookq')
    id=request.GET.get('id')
    book=TBook.objects.get(id=id)
    name=request.GET.get('name')
    print(name)
    if name:
        return render(request,'Book details.html',{'book':book,'name':name})
    return render(request, 'Book details.html', {'book': book})

def book_list(request):
    request.session['url']=request.get_full_path()
    id=request.GET.get('id')
    level=request.GET.get('level')
    num=int(request.GET.get('num',1))
    name=request.GET.get('name')
    if level=='2':
        book=TBook.objects.filter(classify_id=id)
        lens=len(book)
        pagetor=Paginator(book,2)
        books=pagetor.page(num)
        if name:
            return render(request, 'booklist.html', {'qbooks': books,'len':lens,'id':id,
                                                 'level':level,'name':name})
        return render(request, 'booklist.html', {'qbooks': books, 'len': lens, 'id': id,
                                                 'level': level,})
    elif level=='1':
        sort=TSorted.objects.filter(parent_id=id)
        qs=TBook.objects.filter(id=100)
        lens=0
        for i in sort:
            classid=str(i.id)
            books=TBook.objects.filter(classify_id=classid)
            lens+=len(books)
            qs = qs|books
        pagetor = Paginator(qs, 2)
        books = pagetor.page(num)
        if name:
            return render(request,'booklist.html',{'qbooks':books,'len':lens,'id':id,
                                               'level':level,'name':name})
        return render(request, 'booklist.html', {'qbooks': books, 'len': lens, 'id': id,
                                                 'level': level})
#离开页面
def uquit(request):
    url0=request.session.get('url')
    url=url0.split('name')[0]
    red=redirect(url)
    red.delete_cookie('name')
    return red

def shopcar(request):
    request.session['url'] = request.get_full_path()
    name=request.GET.get('name')
    if name:
        userid = TUser.objects.get(username=name).id
        if request.session.get('car'):
            books=request.session.get('car').booklist
            car=Car()
            for  i in books:
                id=i.id
                nums=int(i.num)
                if ShopCart.objects.filter(user_id=userid):
                    if ShopCart.objects.filter(user_id=userid,shop_id=id):
                        t=ShopCart.objects.get(user_id=userid,shop_id=id)
                        t.number+=nums
                        t.save()
                    else:
                        ShopCart.objects.create(user_id=userid,shop_id=id,number=nums)
                else:
                    ShopCart.objects.create(user_id=userid, shop_id=id, number=nums)
            books=car.booklist
            request.session['car']=''
            return render(request,'car.html',{'books':books,'name':name})
        else:
            if ShopCart.objects.filter(user_id=userid):
                car = Car()
                for i in ShopCart.objects.filter(user_id=userid):
                    id=i.shop_id
                    bnum=int(i.number)
                    car.addbook(id,bnum)
                books=car.booklist
                return render(request,'car.html',{'name':name,'books':books})
        return render(request, 'car.html',{'name':name})
    else:
        if request.session.get('car'):
            books=request.session.get('car').booklist
            return render(request,'car.html',{'books':books})
        return render(request, 'car.html')

def addbook(request):
    name=request.GET.get('name')
    id=request.GET.get('id')
    num=int(request.GET.get('num'))
    if name:
        userid=TUser.objects.get(username=name).id
        if request.session.get('car'):
            booklis=request.session.get('car').booklist
            for i in booklis:
                bookid=i.id
                numbers=int(i.num)
                if ShopCart.objects.filter(user_id=userid):
                    if ShopCart.objects.filter(user_id=userid,shop_id=bookid):
                        t=ShopCart.objects.get(user_id=userid,shop_id=bookid)
                        t.number+=numbers
                        t.save()
                    else:
                        ShopCart.objects.create(user_id=userid,shop_id=bookid,number=numbers)
                else:
                    ShopCart.objects.create(user_id=userid, shop_id=bookid, number=numbers)
            request.session['car']=''
            if request.GET.get('type'):
                car = Car()
                for i in ShopCart.objects.filter(user_id=userid):
                    id=i.shop_id
                    bnum=int(i.number)
                    car.addbook(id,bnum)
                books=car.booklist
                return render(request,'car.html',{'name':name,'books':books})
            return HttpResponse('添加成功')
        else:
            if ShopCart.objects.filter(user_id=userid, shop_id=id):
                t=ShopCart.objects.filter(user_id=userid, shop_id=id)[0]
                t.number+=num
                t.save()
                car = Car()
                for i in ShopCart.objects.filter(user_id=userid):
                    id=i.shop_id
                    bnum=int(i.number)
                    car.addbook(id,bnum)
                books=car.booklist
                if request.GET.get('type'):
                    return render(request,'car.html',{'name':name,'books':books})
                return HttpResponse('添加成功')
            else:
                car=Car()
                ShopCart.objects.create(user_id=userid,shop_id=id,number=num)
                for i in ShopCart.objects.filter(user_id=userid):
                    id=i.shop_id
                    bnum=int(i.number)
                    car.addbook(id,bnum)
                books=car.booklist
                if request.GET.get('type'):
                    return render(request,'car.html',{'name':name,'books':books})
                return HttpResponse('添加成功')
    else:
        car=request.session.get('car')
        if not car:
            car=Car()
        car.addbook(id,num)
        request.session['car']=car
        if request.GET.get('type'):
            return redirect(reverse('home:shopcar')+'?name='+name)
        return HttpResponse('添加成功')

def update(request):
    num=int(request.GET.get('num'))
    id=request.GET.get('id')
    name=request.GET.get('name')
    print(num)
    if name:
        userid=TUser.objects.get(username=name).id
        t=ShopCart.objects.filter(user_id=userid,shop_id=id)[0]
        t.number=num
        t.save()
        return HttpResponse(1)
    else:
        car = request.session.get('car')
        if car:
            car.updatenum(id,num)
            request.session['car'] = car
            return HttpResponse(1)
        return HttpResponse(8)

def delbook(request):
    name=request.GET.get('name')
    id=request.GET.get('id')
    print(id)
    types = request.GET.get('type')
    if name:
        userid=TUser.objects.get(username=name)
        ShopCart.objects.filter(user_id=userid,shop_id=id).delete()
        return HttpResponse('1')
    else:
        car=request.session.get('car')
        car.delbook(id)
        request.session['car']=car
        car1 = request.session.get('car')
        books=car1.booklist
        if types:
            return HttpResponse('1')
        return  render(request,'car.html',{'books':books})

class Order:
    def __init__(self,num,bname,press,bprice):
        self.num,self.name=num,bname
        self.price,self.press=bprice,press

def indent(request):
    name=request.GET.get('name')
    request.session['url']=reverse('home:showindent')
    ls = []
    if name:
        nameid=TUser.objects.filter(username=name)[0].id
        cars=ShopCart.objects.filter(user_id=nameid)
        for i in cars:
            booknum = i.number
            book = TBook.objects.get(id=i.shop_id)
            bookname = book.book_name
            press = book.press
            bookprice = book.dd_price
            order = Order(booknum, bookname, press, bookprice)
            ls.append(order)
        request.session['ls'] = ls
    count1=request.GET.get('count1')
    request.session['count1']=count1
    # print(name,nameid,cars,count1)
    if name:
        return HttpResponse(reverse('home:showindent')+'?name='+name)
    return HttpResponse(reverse('login:login'))

def showindent(request):
    name=request.GET.get('name')
    if name:
        nameid=TUser.objects.filter(username=name)[0]
    addrs=TAddress.objects.filter(user_id=nameid)
    count1=request.session.get('count1')
    ls=request.session.get('ls')
    return render(request, 'indent.html',{'addrs':addrs,'name':name,'nameid':nameid,'ls':ls,'count1':count1})


def ajaxshow(request):
    id=request.GET.get('id')
    addr=TAddress.objects.get(id=id)
    def chang(u):
        if isinstance(u,TAddress):
            return {
                'id': u.id,
                'name': u.name,
                'detail_address': u.detail_address,
                'cell_phone_number': str(u.cell_phone_number),
                'fixed_line_telephone': u.fixed_line_telephone,
                'postalcode':u.postalcode,
            }

    return JsonResponse({'addrs': addr}, safe=False, json_dumps_params={'default': chang})
    # return HttpResponse(1111111111)
def ddtiaj(request):
    return HttpResponse(1)

def ddtj(request):
    ordernum=''.join(random.sample(string.digits*10,11))
    count1=request.session.get('count1')
    print(count1)
    shoppeo=request.GET.get('nichen')
    name=request.GET.get('name')
    userid=TUser.objects.get(username=name).id
    car=ShopCart.objects.filter(user_id=userid).delete()
    detaddr=request.GET.get('addr')
    addrid1=TAddress.objects.filter(detail_address=detaddr)
    if addrid1:
        addrid = TAddress.objects.filter(detail_address=detaddr)[0].id
    code=request.GET.get('code')
    namphonee=request.GET.get('phone')
    fixphe=request.GET.get('fixphe')
    if not TAddress.objects.filter(name=shoppeo,detail_address=detaddr,postalcode=code,cell_phone_number=namphonee,fixed_line_telephone=fixphe,user_id=userid):
        TAddress.objects.create(name=shoppeo, detail_address=detaddr, postalcode=code, cell_phone_number=namphonee,
                                fixed_line_telephone=fixphe,user_id=userid)
    TOrder.objects.create(order_number=ordernum,user_id=userid,address_id=addrid,all_price=count1)
    # cars=ShopCart.objects.filter(user_id=userid)
    # for i in cars:
    #     num=i.number
    #     bookid=i.shop_id
    return render(request,'indent ok.html',{'name':name,'ordernum':ordernum,'money':count1})