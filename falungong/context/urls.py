"""falungong URL Configuration

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
from django.urls import path, include
from context import views
app_name='context'
urlpatterns = [
    path('show_context/',views.show_context,name='show_context'),
    path('get_context/',views.get_context,name='get_context'),
    path('uppic/',views.uppic,name='uppic'),
    path('pic_history/',views.pic_history,name='pic_history'),
    path('option_context/',views.option_context,name='option_context'),
    path('save_context/',views.save_context,name='save_context'),
]
