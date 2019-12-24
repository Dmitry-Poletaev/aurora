from django.contrib import admin
from .models import Category, Product
from import_export.admin import ExportActionMixin



# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'slug', 'price',
                    'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated','category')
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    



    