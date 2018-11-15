from django.shortcuts import render

from .models import *

# Create your views here.

#Выводит список ГОСТ_ов сортамента
def sortament(request):
    """Имена переменной и модели должны быть разными"""
    gost = gost_sortamenta.objects.all().order_by("-type")
    context = {
        'gost_sortamenta': gost
    }
    return render(request, 'sortament/sortament.html', context)

# Переход на нужный ГОСТ
# Переход по многим таблицам БД
def perehod_na_gost(request, sortamenta_id):
    text = gost_sortamenta.objects.get(id=sortamenta_id)
    table_10704_91 = text.truby_gost_10704_91_set.all()
    table_8239_89 = text.dvutavr_gost_8239_89_set.all()
    context = {
        'naz_i_img_gostov' : text,
        'table_10704_91' : table_10704_91,
        'table_8239_89' : table_8239_89,
    }
    return render(request, 'sortament/template_sortamenta.html', context)


# def tovar_prodavca(request, id_prodavca):
#     Name_prodavca = prodavcy.objects.get(id=int(id_prodavca))
#     tovar_prodavca = Name_prodavca.tovar_set.order_by('Data')
#     context = {
#         'Name_prodavca' : Name_prodavca,
#         'tovar_prodavca' : tovar_prodavca
#     }
#     return render(request, 'baza_dannyh_sojya_polka/prodavec_s_ego_tovarom.html', context)