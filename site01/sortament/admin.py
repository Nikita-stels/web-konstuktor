from django.contrib import admin
from .models import truby_gost_10704_91, gost_sortamenta, dvutavr_gost_8239_89


# Register your models here.

class truby_gost_10704_91Admin(admin.ModelAdmin):
    # list_display указывает какие поля отображать на админ страницы списка объектов
    list_display = [field.name for field in truby_gost_10704_91._meta.fields]
    search_fields = ["Diametr"]

class Meta:
    model = truby_gost_10704_91


admin.site.register(truby_gost_10704_91, truby_gost_10704_91Admin)


# отдельный класс
class dvutavr_gost_8239_89Admin(admin.ModelAdmin):
    # list_display указывает какие поля отображать на админ страницы списка объектов
    list_display = [field.name for field in dvutavr_gost_8239_89._meta.fields]


class Meta:
    model = dvutavr_gost_8239_89


admin.site.register(dvutavr_gost_8239_89, dvutavr_gost_8239_89Admin)


# отдельный класс название ГОСТов
class gost_sortamentaAdmin(admin.ModelAdmin):
    # list_display указывает какие поля отображать на админ страницы списка объектов
    #list_display = ["id", "img_gost", "GOST", "type", "Gost_naz"]
    list_display = [ field.name for field in gost_sortamenta._meta.fields ]


class Meta:
    model = gost_sortamenta


admin.site.register(gost_sortamenta, gost_sortamentaAdmin)
