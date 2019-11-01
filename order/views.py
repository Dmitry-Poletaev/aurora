from django.shortcuts import render
from .models import Order, OrderItem
from .forms import OrderForm
from cart.cart import Cart
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
#def checkout_view(request):
    #form = OrderForm(request.POST)
    #if request.method == 'POST':
       # if form.is_valid():
        #    form.save()
        #    return HttpResponseRedirect('thanks/')
        
    #return render(request, 'checkout.html', {'form': form})


#def thanks(request):
    #return render(request, 'thanks.html')


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
            # launch asynchronous task
            #order_created.delay(order.id)
            return render(request,
                          'thanks.html',
                          {'order': order})
    else:
        form = OrderForm()
    return render(request,
                  'checkout.html',
                  {'cart': cart, 'form': form})