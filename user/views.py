import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from note.models import Note
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

@csrf_exempt
def get_info(request):
    username = request.POST.get('username')
    user = User.objects.filter(username=username).first()
    if user:
        return JsonResponse({
            'username': user.username,
            'avatar': user.avatar,
            'signature': user.signature
        })
    else:
        return HttpResponse('failure')

@csrf_exempt
def set_info(request):
    data = json.loads(request.body)
    old_username = data.get('old_username')
    new_username = data.get('new_username')
    avatar = data.get('avatar')
    signature = data.get('signature')
    user = User.objects.filter(username=old_username).first()
    if user:
        user.username = new_username
        user.avatar = avatar
        user.signature = signature
        user.save()
         # 修改笔记表中的username
        Note.objects.filter(username=old_username).update(username=new_username)
        return HttpResponse('success')
    else:
        return HttpResponse('failure')


@csrf_exempt
def get_avatar(request):
    data = json.loads(request.body)
    username = data.get('username')
    print(username)
    user = User.objects.filter(username=username).first()
    if user:
        return JsonResponse({
            'avatar': user.avatar
        })
    else:
        return HttpResponse('failure')

@csrf_exempt
def change_password(request):
    username = request.POST.get('username')
    old_password = request.POST.get('old_password')
    new_password = request.POST.get('new_password')
    print(username,old_password,new_password)
    user = User.objects.filter(username=username,password=old_password).first()
    if user:
        user.password = new_password
        user.save()
        return HttpResponse('success')
    else:
        return HttpResponse('failure',status=404)
