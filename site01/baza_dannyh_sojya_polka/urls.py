from django.urls import path, re_path

# Импортируем все функции из текущего каталога (из views)
from .views import *

urlpatterns = [

    path('', prodavcy_na_polki, name='prodavcy_na_polki'),
    re_path(r'^(?P<id_prodavca>\d+)/$', tovar_prodavca, name='tovar_prodavca'),

]
