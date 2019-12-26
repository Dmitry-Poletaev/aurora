from django.contrib import admin
from .models import Order, OrderItem
from django.utils.safestring import mark_safe
from django.urls import reverse


# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    def order_pdf(self):
        return mark_safe('<a href="{}">PDF</a>'.format(
            reverse('orders:admin_order_pdf', args=[self.id])))
        order_pdf.short_description = 'Invoice'

    list_display = ['id', 'name', 'email',
                    'created_date', 'updated',order_pdf]
    list_filter = ['paid', 'created_date']
    inlines = [OrderItemInline]
    