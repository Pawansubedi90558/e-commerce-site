from django.urls import path
from django.shortcuts import HttpResponse

from core import index

def home(request):
    return HttpResponse(request,'index.html')