# Generated by Django 2.1.1 on 2018-10-10 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sortament', '0011_auto_20181010_1027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dvutavr_gost_8239_89',
            options={'verbose_name': 'Двутавр по ГОСТ 8239-89', 'verbose_name_plural': 'Двутавры по ГОСТ 8239-89'},
        ),
        migrations.AlterModelOptions(
            name='gost_sortamenta',
            options={'verbose_name': 'ГОСТ Сортамента', 'verbose_name_plural': 'ГОСТы Сортаментов'},
        ),
        migrations.AlterModelOptions(
            name='truby_gost_10704_91',
            options={'verbose_name': 'Трубу по ГОСТ 10704-91', 'verbose_name_plural': 'Трубы по ГОСТ 10704-91'},
        ),
    ]