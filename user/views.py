from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from user.models import User

@csrf_exempt
def login(request):
    # 获取请求参数
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username,password)
    # 查询数据库
    user = User.objects.filter(username=username,password=password)
    if user:
        return HttpResponse('success')
    else:
        return HttpResponse('failure')
    pass

@csrf_exempt
def register(request):
    # your code here
    username = request.POST.get('username')
    password = request.POST.get('password')
    telephone = request.POST.get('telephone')
    print(username,password,telephone)
    # 查询数据库
    user = User.objects.filter(username=username)
    if user:
        return HttpResponse('failure, username already exists')
    else:
        User.objects.create(username=username,password=password,phone=telephone)
        return HttpResponse('success')
    pass