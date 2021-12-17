# -*- coding = utf-8 -*
# @Author: younFuns
# @Time : 2021/12/15 21:33
# @File : urls
# @Product : PyCharm

from django.urls import path
from goods import views

urlpatterns = [
    path('goods/', views.operation_goods)
]
