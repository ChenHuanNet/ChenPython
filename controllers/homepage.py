
from django.shortcuts import HttpResponse
from django.shortcuts import render
import requests
def index(request):
    context = {}
    if "a" in request.GET:#判断一个关键字是否在字典中
        context['query'] = request.GET['a']

    return render(request, "homepage/index.html", context)
