from django.db import models

# Create your models here.


# Модель для названий ГОСТов и хранения изобродений поперечного сечения
class gost_sortamenta(models.Model):
    PERECHEN_SORTAMENTA = (
        ('Труба', 'Труба'),
        ('Двутавр', 'Двутавр'),
    )

    """Сортамент"""
    GOST = models.CharField(max_length=250,
                            verbose_name='Название ГОСТа')
    img_gost = models.ImageField(upload_to='sortament/',
                                 verbose_name='Изображение')
    type = models.CharField(max_length=250,
                            choices=PERECHEN_SORTAMENTA,
                            verbose_name='Тип проката'
                            )

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.GOST

    # Изменение названия в админки (одиночное и множественное)
    class Meta:
        verbose_name = 'ГОСТ Сортамента'
        verbose_name_plural = 'ГОСТы Сортаментов'
# Модель для трубы по ГОСТ 10704_91
class truby_gost_10704_91(models.Model):
    """Характеристики сорамента"""
    Diametr = models.FloatField(verbose_name='d-диаметр')
    Tolshuna_stenki = models.FloatField(verbose_name='t-толщина стенки ')
    Ploshad_poperechnogo_sech = models.FloatField()
    Moment_inercii = models.FloatField()
    Moment_soprotivleniya = models.FloatField()
    Statisticheskiy_moment = models.FloatField()
    Radius_inercii = models.FloatField()
    Massa_v_pog_metre = models.FloatField()
    # мы указали атрибуты blank=True и null=True, поэтому сразу после создания
    # новый столбец будет содержать NULL во всех записях таблицы.
    # Установите значение ForeignKey null; это возможно только если null is True.
    Nomer_gosta = models.ForeignKey(
        gost_sortamenta,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Номер госта")

    """Возвращает с плавующей точкой представление модели."""
    def __float__(self):
        return self.Diametr
    #Изменение названия в админки (одиночное и множественное)
    class Meta:
        verbose_name = 'Трубу по ГОСТ 10704-91'
        verbose_name_plural = 'Трубы по ГОСТ 10704-91'

# Модель для двутавра по ГОСТ 8239_89
class dvutavr_gost_8239_89(models.Model):
    """Сортамент"""
    nomer_dvutavra = models.IntegerField(verbose_name='Номер')
    vysota_h = models.IntegerField(verbose_name = "Высота")
    shirina_pilki_b = models.IntegerField(verbose_name = "Ширина")
    tolshina_stenki_s = models.FloatField(verbose_name = "Толщина")
    srednyaya_tolsina_polki_t = models.FloatField(verbose_name = "Сред толщ")
    radius_vnutrennego_zakrugleniya_R = models.FloatField(verbose_name = "Радиус внут")
    radius_zakrugleniya_polki_r = models.FloatField(verbose_name = "Радиус зак полки")
    ploshad_poer_sech_A = models.FloatField()
    massa_m = models.FloatField()
    mom_iner_Ix = models.IntegerField()
    mom_sopr_Wx = models.FloatField()
    radius_iner_i_x = models.FloatField()
    stat_mom_polu_sech_Sx = models.FloatField()
    mom_iner_Iy = models.FloatField()
    mom_sopr_Wy = models.FloatField()
    radius_iner_i_y = models.FloatField()
    Nomer_gosta = models.ForeignKey(
        gost_sortamenta,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Номер госта")

    """Возвращает с плавующей точкой представление модели."""
    def __int__(self):
        return self.nomer_dvutavra

    # Изменение названия в админки (одиночное и множественное)
    class Meta:
        verbose_name = 'Двутавр по ГОСТ 8239-89'
        verbose_name_plural = 'Двутавры по ГОСТ 8239-89'