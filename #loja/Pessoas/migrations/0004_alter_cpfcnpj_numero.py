# Generated by Django 4.0.4 on 2022-04-21 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoas', '0003_cpfcnpj_cliente_cpf_cnpj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpfcnpj',
            name='numero',
            field=models.CharField(max_length=14, unique=True),
        ),
    ]
