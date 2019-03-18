
from django.shortcuts import HttpResponse
from django.shortcuts import render
#requests包是用来做各种http请求的
import requests
import DB.mysqlhelper

def index(request):
    context = {}
    if "a" in request.GET:#判断一个关键字是否在字典中
        context['query'] = request.GET['a']
    #操作mysql数据库
    DB.mysqlhelper.ExecuteSql('');
    return render(request, "homepage/index.html", context)
