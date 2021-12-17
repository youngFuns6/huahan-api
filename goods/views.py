import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from goods.models import Goods

# Create your views here.

# 分发处理逻辑
def operation_goods(request):
    if request.method == "GET":
        return getGoods(request)
    elif request.method == "POST":
        return addGoods(request)
    elif request.method == "PUT":
        return editGoods(request)
    elif request.method == "DELETE":
        return deleteGoods(request)
    else:
        return JsonResponse({
            "code": 1001,
            "msg": "系统错误"
        })

# 获取商品
def getGoods(request):
    # 查询表记录
    qs = Goods.objects.values()
    print(qs)
    ret = list(qs)
    return JsonResponse({
        "code": 200,
        "msg": "success",
        "data": ret
    })

# 添加商品
def addGoods(request):
    _type = request.POST.get("type")
    title = request.POST.get("title")
    desc = request.POST.get("desc")
    banner = request.POST.get("type")

    # 插入数据
    record = Goods.objects.create(type=_type, title=title, desc=desc, banner=banner)
    # print(record)
    return JsonResponse({
        "code": 200,
        "msg": "success",
        "data": record.id
    })

# 编辑商品
def editGoods(request):
    return JsonResponse('获取商品列表')

# 删除商品
def deleteGoods(request):
    return JsonResponse('获取商品列表')
