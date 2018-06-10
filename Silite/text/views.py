from django.shortcuts import render
# coding:utf-8
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def add2(request, a, b):
    return HttpResponse(str(int(a) + int(b)))
def index(request):
    return render(request, 'home.html')