from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Order, OrderItem
from .forms import OrderForm
from product.models import Category
from cart.cart import Cart
from .tasks import order_created, admin_notification
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
import weasyprint


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('order.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\
                    "заказ№{}.pdf"'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response)
                        
    return response

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # Запуск асинхронной задачи.
            order_created(order.id)
            #admin_notification(order.id)
            #order_created.delay(order.id)
            return render(request,
                          'thanks.html',
                          {'order': order})
    else:
        form = OrderForm()
    return render(request,
                  'checkout.html',
                  {'cart': cart, 'form': form, 'categories':Category.objects.all()})

