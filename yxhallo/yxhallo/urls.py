"""yxhallo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,re_path

from . import view,testdb


urlpatterns = [
    re_path('hello', view.hello,name='hello'),
    re_path('say',view.say,name='say'),
    re_path('runoob',view.runoob),
    re_path('varname',view.varname),
    re_path('dicttest',view.vardict),
    re_path('time',view.vardatetime,name='time'),
    re_path('dump',view.urldump),
    re_path('readdict',view.vardict),
    re_path('testdb',testdb.testdb)
]