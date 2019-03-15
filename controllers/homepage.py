
from django.shortcuts import HttpResponse
from django.shortcuts import render
import requests
def index(request):
    context = {}

    return render(request, "homepage/index.html", context)
