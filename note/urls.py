from django.urls import path
from . import views

urlpatterns = [
    path('store_note/', views.store_note, name='store_note'),
    path('get_note/', views.get_note, name='get_note'),
    path('get_all_notes/', views.get_all_notes, name='get_all_notes'),
    path('change_note/', views.change_note, name='change_note'),
    path('filter_note/', views.filter_note, name='filter_note'),
    path('wenxin_note/', views.wenxin_note, name='wenxin_note'),
]