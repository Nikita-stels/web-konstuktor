from django.shortcuts import render
# Импорт всех моделей из данного каталога
from .models import *
from django.http import HttpResponse


# Create your views here.

# Выводит список всех продавцов на полке
def prodavcy_na_polki(request):
    """Имена переменной и модели должны быть разными"""
    prodavcy_na_polki = prodavcy.objects.all().order_by("Name")
    context = {
        'prodavcy_na_polki': prodavcy_na_polki
    }
    return render(request,
                  'baza_dannyh_sojya_polka/baza_dannyh_sojya_polka.html',
                  context)


# Переход на определенного родавца с его товаром
def tovar_prodavca(request, id_prodavca):
    Name_prodavca = prodavcy.objects.get(id=int(id_prodavca))
    tovar_prodavca = Name_prodavca.tovar_set.order_by('Data')
    context = {
        'Name_prodavca': Name_prodavca,
        'tovar_prodavca': tovar_prodavca
    }
    return render(request,
                  'baza_dannyh_sojya_polka/prodavec_s_ego_tovarom.html',
                  context)
    # return HttpResponse(Name_prodavca.Name)
