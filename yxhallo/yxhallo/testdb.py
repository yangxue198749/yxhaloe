# -*- coding: utf-8 -*-
# @Time    : 2020/11/16 14:50
# @Author  : yangxue
# @Email   : yangxue@xiyun.com.cn
# @File    : testdb.py

from django.http import HttpResponse
from yxhallo.TestModel.models import yxTest

def testdb(request):
    test1 = yxTest(name='runoob')
    test1.save()
    return HttpResponse("<p>数据y添加成功！</p>")