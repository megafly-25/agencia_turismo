# Generated by Django 2.2.6 on 2021-07-03 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paquete_turistico_agencia',
            name='servicio',
        ),
        migrations.AddField(
            model_name='paquete_turistico_agencia',
            name='servicio',
            field=models.ManyToManyField(to='main.Servicios_agencia'),
        ),
    ]
