# Generated by Django 2.1.1 on 2018-10-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='spisok_raschetov',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nazvanie', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('КЖ', 'КЖ'), ('КМ', 'КМ'), ('Сортаменты металлопроката', 'Сортаменты металлопроката')], max_length=250)),
            ],
            options={
                'verbose_name': 'Характеристики расчёта',
                'verbose_name_plural': 'Характеристики расчётов',
            },
        ),
    ]
