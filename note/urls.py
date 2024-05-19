from django.urls import path
from . import views

urlpatterns = [
    path('store_note/', views.store_note, name='store_note'),
    path('get_note/', views.get_note, name='get_note')
]