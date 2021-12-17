from django.db import models

# Create your models here.


class User(models.Model):
    # 用户名
    username = models.CharField(max_length=11, primary_key=True)

    # 密码
    password = models.CharField(max_length=16)
