# Generated by Django 2.2.5 on 2019-10-29 06:42

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название')),
                ('slug', models.SlugField(max_length=120, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('banner', models.ImageField(blank=True, upload_to='images/', verbose_name='Баннер')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Title')),
                ('description_seo', models.CharField(blank=True, max_length=140, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, upload_to='images/', verbose_name='Изображение')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена со скидкой')),
                ('sale', models.IntegerField(blank=True, default=0, null=True, verbose_name='Скидка в процентах')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('available', models.BooleanField(blank=True, default=True, verbose_name='В наличии')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Title')),
                ('description_seo', models.CharField(blank=True, max_length=140, verbose_name='Description')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['price', 'discount_price'],
            },
        ),
    ]
