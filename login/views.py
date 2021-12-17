import json

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def sign(request):
    userName = request.POST.get("username")
    passWord = request.POST.get("password")
    print(userName)
    # 校验用户名 密码
    user = authenticate(username=userName, password=passWord)

    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                request.session['usertype'] = 'manager'
                return JsonResponse({"code": 200, "msg": "success"})
            else:
                return JsonResponse({
                    "code": 1001,
                    "msg": "请使用管理员账号登录"
                })
        else:
            return JsonResponse({
                "code": 1002,
                "msg": "用户已被禁用"
            })
    else:
        return JsonResponse({
            "code": 1003,
            "msg": "账号或密码错误"
        })

def signout(request):
    logout(request)
    return JsonResponse({
        "code": 0,
        "msg": "退出登录成功"
    })