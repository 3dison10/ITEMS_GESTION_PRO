# Generated by Django 5.0.6 on 2024-06-10 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itemsproapp', '0004_alter_usuarios_teladmon'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='usuarios',
            new_name='cliente',
        ),
    ]