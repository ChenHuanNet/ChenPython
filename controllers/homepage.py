
from django.shortcuts import HttpResponse
from django.shortcuts import render
import requests
def index(request):
    context = {}
    context['a']=request.GET['a']
    return render(request, "homepage/index.html", context)
