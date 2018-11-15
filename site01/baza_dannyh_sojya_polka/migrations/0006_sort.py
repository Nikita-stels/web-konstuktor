# Generated by Django 2.1.2 on 2018-10-23 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza_dannyh_sojya_polka', '0005_delete_gost'),
    ]

    operations = [
        migrations.CreateModel(
            name='sort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GOST', models.CharField(max_length=250, verbose_name='Название ГОСТА')),
                ('Nomer_Gosta', models.CharField(max_length=250, verbose_name='Номер госта')),
            ],
            options={
                'verbose_name': 'ГОСТ',
                'verbose_name_plural': 'ГОСТы',
            },
        ),
    ]