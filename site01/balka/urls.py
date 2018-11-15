from django.urls import path
# Импортируем все функции из текущего каталога (из views)
from .views import *

# Устаревшее
# from django.conf.urls import url
# from balka import views

urlpatterns = [
    path('', balka, name='balka'),
    path('balkaras/', balkaras, name='balkaras/'),

    # Устаревшее
    # url(r'^$', views.balka, name='balka'),
    # url(r'^balkaras/', views.balkaras, name='balkaras'),
]