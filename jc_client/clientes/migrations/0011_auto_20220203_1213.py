# Generated by Django 2.2 on 2022-02-03 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_auto_20220203_1211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['-data_nascimento']},
        ),
    ]
