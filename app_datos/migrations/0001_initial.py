# Generated by Django 4.0.4 on 2022-05-30 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudadano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('ciudad', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Dispositivos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.CharField(max_length=40)),
                ('computadora', models.CharField(max_length=40)),
                ('tablet', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tiempo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias', models.IntegerField()),
                ('horas', models.IntegerField()),
            ],
        ),
    ]
