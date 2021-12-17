from django.db import models


# Create your models here.

class Goods(models.Model):
    # 商品类别
    type = models.IntegerField(primary_key=True)
    # 商品名称
    title = models.CharField(max_length=100)
    # 商品描述
    desc = models.TextField()
    # 商品图片
    banner = models.CharField(max_length=200)
    # 创建时间
    created = models.DateTimeField(auto_now_add=True, null=True)
    # 更新时间
    # modified = models.DatedTimeField(autro_now=True)
