from django.contrib import admin
from .models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name','created_date',)
    list_filter = []
    


admin.site.register(Order, OrderAdmin)