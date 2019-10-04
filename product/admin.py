from django.contrib import admin
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','price','created_date','updated_at',)
    list_filter = ['category','available']
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
