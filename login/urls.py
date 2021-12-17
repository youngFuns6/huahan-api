# -*- coding = utf-8 -*
# @Author: younFuns
# @Time : 2021/12/17 21:17
# @File : urls
# @Product : PyCharm

from django.urls import path
from login import views

urlpatterns = [
    path('login', views.sign),
    path('logout', views.signout)
]