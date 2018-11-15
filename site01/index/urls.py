from django.urls import path
# Импортируем все функции из текущего каталога (из views)
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('spisok/', spisok_ras, name='spisok_ras'),

]