# Generated by Django 2.2.5 on 2019-10-09 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_order_delivery_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_choice',
        ),
    ]
