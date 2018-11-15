from django.contrib import admin

from .models import spisok_raschetov

# Register your models here.

# отдельный класс название ГОСТов
class spisok_raschetovAdmin(admin.ModelAdmin):
    # list_display указывает какие поля отображать на админ страницы списка объектов
    list_display = [ field.name for field in spisok_raschetov._meta.fields ]


class Meta:
    model = spisok_raschetov


admin.site.register(spisok_raschetov, spisok_raschetovAdmin)