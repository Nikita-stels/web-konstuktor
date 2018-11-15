"""site01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path

# Устаревшее
from django.conf.urls import url
from django.contrib import admin

#привязывает заданную в переменной МEDIA RООТ папку к заданному в переменной МEDIA URL префиксу интернет-адресов
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Подключение наших приложений к проекту
    # path появилось в новой версии Django docs.djangoproject.com/en/2.1/ref/urls/#django.urls.path
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('izgib_balki/', include('balka.urls')),
    path('armatura/', include('armatura.urls')),
    path('sortament/', include('sortament.urls')),
    path('prodavcy/', include('baza_dannyh_sojya_polka.urls')),
    path('specifikaciy/', include('spec_kamery.urls')),

# Устаревшие пути
    # url(r'^admin/', admin.site.urls),
    # url(r'', include('index.urls')),
    # url(r'^izgib_balki/', include('balka.urls')),
    # url(r'^armatura/', include('armatura.urls')),
    # url(r'^sortament/', include('sortament.urls')),
] \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# привязывает заданную в переменной МEDIA RООТ папку к заданному в переменной МEDIA URL префиксу интернет-адресов
