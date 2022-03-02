# Generated by Django 2.2 on 2022-01-27 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20220126_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=100)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='produtos',
            field=models.ManyToManyField(to='clientes.Produto'),
        ),
    ]