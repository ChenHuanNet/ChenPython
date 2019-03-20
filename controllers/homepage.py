from django.shortcuts import HttpResponse
from django.shortcuts import render
# requests包是用来做各种http请求的
import requests
import DB.mysqlhelper

from django.conf import settings


def index(request):
    context = {}
    id = "0"
    if "id" in request.GET:  # 判断一个关键字是否在字典中
        context['query'] = 'id:' + request.GET['id']
        id = request.GET['id']

    # 操作mysql数据库
    sql = (" select * from ord_user_list where Id=%s " % id)
    user = DB.mysqlhelper.GetDict(sql)
    if user is None:
        user = '空'  # python是一种弱类型语言 变量类型可以随便替换的 跟JS一样
    user2 = DB.mysqlhelper.Get(sql)
    context["user"] = user
    context["user2"] = user2

    sql = (" select * from ord_user_list limit 10 ")
    user3 = DB.mysqlhelper.Gets(sql)
    context["user3"] = user3
    user4 = DB.mysqlhelper.GetsDict(sql)
    context["user4"] = user4

    nickname = ''
    if "nickname" in request.GET:
        nickname = request.GET['nickname']
    # sql = " update ord_user_list set NickName='%s' where Id=1 "%nickname
    sql = " update ord_user_list set NickName=%s where Id=1 "
    rows = DB.mysqlhelper.ExecuteSql(sql, [nickname])
    context['rows'] = rows
    return render(request, "homepage/index.html", context)
