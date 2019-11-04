from django.shortcuts import render
from .models import Order, OrderItem
from .forms import OrderForm
from cart.cart import Cart
from django.http import HttpResponseRedirect, HttpResponse
from .tasks import order_created





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
            order_created.delay(order.id)
            #order_created.delay(order.id)
            return render(request,
                          'thanks.html',
                          {'order': order})
    else:
        form = OrderForm()
    return render(request,
                  'checkout.html',
                  {'cart': cart, 'form': form})