from django.db import models

# Create your models here.

#Модель для списка расчетов
class spisok_raschetov (models.Model):
    """Характеристики расчётов"""
    PERECHEN_SORTAMENTA = (
        ('КЖ', 'КЖ'),
        ('КМ', 'КМ'),
        ('Сортаменты металлопроката', 'Сортаменты металлопроката'),
    )

    Nazvanie = models.CharField(max_length=250)
    type = models.CharField(max_length=250, choices=PERECHEN_SORTAMENTA)
    url_rascheta = models.CharField(max_length=250)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.Nazvanie

    # Изменение названия в админки (одиночное и множественное)
    class Meta:
        verbose_name = 'Характеристики расчёта'
        verbose_name_plural = 'Характеристики расчётов'