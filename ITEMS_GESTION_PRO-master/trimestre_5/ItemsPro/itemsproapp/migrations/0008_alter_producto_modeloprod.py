# Generated by Django 5.0.4 on 2024-06-23 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemsproapp', '0007_rename_modelo_producto_id_producto_fotoprod_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='modeloProd',
            field=models.CharField(default='Ingrese Modelo', max_length=50, verbose_name='Modelo del Producto'),
        ),
    ]
