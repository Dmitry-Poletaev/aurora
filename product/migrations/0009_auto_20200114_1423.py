# Generated by Django 2.2.8 on 2020-01-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20191203_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
    ]
