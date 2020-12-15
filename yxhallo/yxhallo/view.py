# -*- coding: utf-8 -*-
# @Time    : 2020/11/4 16:22
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : view.py

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("Hello world ! ")


def say(request):
    return HttpResponse('say!')

def runoob(request):
    context={}
    context['hello1']='hello world!! gg'
    context['say']='say' \
                   ''
    return (render(request,'runoob.html',context))

def varname(request):
    kk=['abc','456','789']
    return render(request,'runoob.html',{'gg':kk})

def vardict(request):
    dict1={'name':'yagnxue','age':16,'sex':'men'}
    return render(request,'runoob.html',{'dict':dict1})

def vardatetime(request):
    import datetime
    now=datetime.datetime.now()
    return render(request,'runoob.html',{'data':now})

def urldump(request):
    url_to="<a href='https://www.baidu.com/'>点击跳转</a>"
    return render(request,'runoob.html',{'views_str':url_to})

def readdict(request):
    dict1 = {'name': 'yagnxue', 'age': 16, 'sex': 'men'}
    return render(request, 'runoob.html', {'dict': dict1})




