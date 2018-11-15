from django.urls import path
# Устаревшее
#from django.conf.urls import url
from .import views

urlpatterns = [
    path('', views.armatura01, name='armatura01'),
    path('input/', views.input, name='input'),

    # Устаревшее
    # url(r'^$', views.armatura01, name='armatura'),
    # url(r'input', views.input, name='input'),
]
