from django.shortcuts import render
from .models import sortam_armatura
from django.http import HttpResponse
# Create your views here.


def armatura01 (request):
    dim = sortam_armatura.objects.all()
    context = {
        'vs_table': dim
    }
    return render(request, 'armatura/armatura.html', context)


#Выборка строки элементов через значение строки
def input (request):
    kluch = int(request.POST['poisk_dim'])
    dim = sortam_armatura.objects.get(Dim = kluch)

    context = {
        'diametr' : dim,
    }

    return render(request, 'armatura/armatura01.html', context)
