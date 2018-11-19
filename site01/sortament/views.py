from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .utils import Mixin

# Выводит список ГОСТов сортамента
# Ссылаемся на Class Basse Views их файла с миксинами (примесь) наследуем часть логики
class Sortament(Mixin, TemplateView):
    model = gost_sortamenta
    tamplate = 'sortament/sortament.html'


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

