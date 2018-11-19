from django.shortcuts import render
from .models import *


# Выводит список ГОСТов сортамента
class Mixin:
    model = None
    tamplate = None

    def get(self, request):
        # Имена переменной и модели должны быть разными
        obj = self.model.objects.all().order_by("-type")
        context = {
            self.model.__name__.lower(): obj
        }
        return render(request, self.tamplate, context)
