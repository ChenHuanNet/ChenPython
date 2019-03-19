
from django.shortcuts import HttpResponse
from django.shortcuts import render
#requests包是用来做各种http请求的
import requests
import DB.mysqlhelper

from django.conf import  settings

def index(request):
    context = {}
    if "a" in request.GET:#判断一个关键字是否在字典中
        context['query'] = request.GET['a']

    print(settings.DATABASES)
    context["defaultmysql"] = settings.DATABASES.get('mysql').get('host')
    print(settings.APPSETTING)
    context["mysql"]=settings.APPSETTING.get('mysql')[0].get('password')
    #操作mysql数据库
    #DB.mysqlhelper.ExecuteSql('');
    return render(request, "homepage/index.html", context)
