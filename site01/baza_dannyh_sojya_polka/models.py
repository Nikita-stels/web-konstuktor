from django.db import models

# Create your models here.
#Модель покупателей

class prodavcy (models.Model):
    """Имя продавца"""
    Name = models.CharField(max_length=250, verbose_name="Имя покупятеля")
    Data = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время")

    """Возвращает с плавующей точкой представление модели."""
    def __str__(self):
        return self.Name
    #Изменение названия в админки (одиночное и множественное)
    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'


#Модель товара
class tovar (models.Model):
    """Товар"""
    Nazvanie_tovara = models.CharField(max_length=250, verbose_name = "Товар")
    price = models.IntegerField(verbose_name = "Цена")
    komu_prenadlejyt_tovar = models.ForeignKey(prodavcy, null = True, blank = True, on_delete = models.SET_NULL, verbose_name = "Продавец")
    Data = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время")

    """Возвращает с плавующей точкой представление модели."""
    def __str__(self):
        return self.Nazvanie_tovara
    #Изменение названия в админки (одиночное и множественное)
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


