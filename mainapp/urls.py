from django.urls import path
from .views import index, subscribe

urlpatterns = [
    path('', index, name='index'),
    path('subscribe/', subscribe, name='subscribe'),
]