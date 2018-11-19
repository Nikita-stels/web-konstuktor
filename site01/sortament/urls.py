from django.urls import path, re_path
# Импортируем все функции из текущего каталога (из views)
from .views import *

# from django.conf.urls import url
# from .import views

urlpatterns = [

    #path('', sortament, name='sortament'),
    path('', Sortament.as_view(), name='sortament'),
    re_path(r'^(?P<sortamenta_id>\d+)/$', perehod_na_gost, name='perehod_na_gost'),

    # Устаревшее
    # url(r'^$', views.sortament, name='sortament'),
    #url(r'^(?P<sortamenta_id>\d+)/$', views.perehod_na_gost, name='perehod_na_gost'),

]
