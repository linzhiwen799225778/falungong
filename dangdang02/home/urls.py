"""dangdang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import home
from home import views

app_name='home'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index,name='index'),
    path('book_detial/', views.book_detial,name='book_detial'),
    path('book_list/', views.book_list,name='book_list'),
    path('uquit/', views.uquit,name='uquit'),
    path('shopcar/', views.shopcar,name='shopcar'),
    path('addbook/', views.addbook,name='addbook'),
    path('update/', views.update,name='update'),
    path('delbook/', views.delbook,name='delbook'),
    path('indent/', views.indent,name='indent'),
    path('showindent/', views.showindent,name='showindent'),
    path('ajaxshow/', views.ajaxshow,name='ajaxshow'),
    path('ddtj/', views.ddtj,name='ddtj'),
    path('ddtiaj/', views.ddtiaj,name='ddtiaj'),
]
