# Generated by Django 4.1.5 on 2023-01-10 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_solicitud',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_reserva',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
