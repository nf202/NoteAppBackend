from django.db import models

# Create your models here.
#创建用户表
class User(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)