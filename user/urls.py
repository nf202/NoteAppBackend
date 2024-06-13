from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('get_info/', views.get_info, name='get_info'),
    path('set_info/', views.set_info, name='set_info'),
    path('get_avatar/', views.get_avatar, name='get_avatar'),
    path('change_password/', views.change_password, name='change_password'),
]