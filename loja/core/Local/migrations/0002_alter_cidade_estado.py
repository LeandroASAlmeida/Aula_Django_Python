# Generated by Django 4.0.6 on 2022-07-06 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Local', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Local.estado'),
        ),
    ]