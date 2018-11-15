from django.shortcuts import render
from index.models import spisok_raschetov

from django.http import HttpResponse

def index(request):
    return render(request, 'index/index.html')

# def index01(request):
#     return render(request, 'index/index01.html')


def spisok_ras(request):
    """Выводит список """
    """Имена переменной и модели должны быть разными"""
    spisok_r = spisok_raschetov.objects.all()
    context = {
        'spisok_raschetov_r': spisok_r
    }
    return render(request, 'index/index01.html', context)
