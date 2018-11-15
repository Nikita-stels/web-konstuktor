from django.urls import path, re_path
# Импортируем все функции из текущего каталога (из views)
from .views import *


urlpatterns = [
    path('', pec_kamery, name='pec_kamery'),


]
