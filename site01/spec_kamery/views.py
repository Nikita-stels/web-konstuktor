from django.shortcuts import render

from .models import *

# Create your views here.

#Выводит список ГОСТ_ов сортамента
def pec_kamery(request):

    return render(request, 'spec_kamery/spec_kamery.html')



