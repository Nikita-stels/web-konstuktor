from django.contrib import admin

# Register your models here.

from .models import prodavcy, tovar

class prodavcyAdmin(admin.ModelAdmin):
    # list_display указывает какие поля отображать на админ страницы списка объектов
    list_display = [field.name for field in prodavcy._meta.fields]
    #Поиск по строкам
    search_fields = ["Name"]

class Meta:
    model = prodavcy

admin.site.register(prodavcy, prodavcyAdmin)

#Подключение модели к админки
class tovarAdmin(admin.ModelAdmin):
    # list_display указывает какие поля отображать на админ страницы списка объектов
    list_display = [field.name for field in tovar._meta.fields]
    #Поиск по строкам
    search_fields = ["komu_prenadlejyt_tovar__Name"]
    list_filter = ["komu_prenadlejyt_tovar"]

class Meta:
    model = tovar

admin.site.register(tovar, tovarAdmin)


