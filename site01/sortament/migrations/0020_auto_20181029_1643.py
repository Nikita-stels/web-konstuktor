# Generated by Django 2.1.2 on 2018-10-29 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sortament', '0019_remove_truby_gost_10704_91_gost_naz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dvutavr_gost_8239_89',
            name='Gost_naz',
        ),
        migrations.AddField(
            model_name='dvutavr_gost_8239_89',
            name='Nomer_gosta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sortament.gost_sortamenta', verbose_name='Номер госта'),
        ),
    ]
