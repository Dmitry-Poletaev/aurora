from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Order, OrderItem
from .forms import OrderForm
from product.models import Category
from cart.cart import Cart
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
import weasyprint
from django.core.mail import EmailMessage
from io import BytesIO


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


def order_created(order_id):
    """
    Отправка e-mail уведомления при успешном оформлении заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Заказ №{order.id}.'
    message = f'Добрый день, {order.name},\nВаш заказ успешно оформлен.\
                  \nНомер вашего заказа {order.id}.\
                  \nИнформация во вложении.'
    email = EmailMessage(subject,
                        message,
                        'd.poletaev@vorteil-technology.ru',
                        [order.email])                                        
     # Формирование PDF
    html = render_to_string('order.html', {'order': order})
    out = BytesIO()
    weasyprint.HTML(string=html).write_pdf(out)
    email.attach('заказ_{}.pdf'.format(order.id),
                                out.getvalue(),
                                'application/pdf')
    email.send()


def admin_notification(order_id):
    """
    Отправка e-mail уведомления администратору при успешном формлении заказа заказа.
    """
   
    order = Order.objects.get(id=order_id)
    subject = f'Заказ №{order.id}.'
    message = f'{order.name} успешно оформил заказ №{order.id}.Информация во вложении.'
    email = EmailMessage(subject,
                        message,
                        'd.poletaev@vorteil-technology.ru',
                            ['d.poletaev@vorteil-technology.ru'])
    # Формирование PDF
    html = render_to_string('order.html', {'order': order})
    out = BytesIO()
    weasyprint.HTML(string=html).write_pdf(out)
    # Прикрепляем PDF к электронному сообщению
    email.attach('заказ_{}.pdf'.format(order.id),
                                out.getvalue(),
                                'application/pdf')

    email.send()


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
            # Очищаем корзину
            cart.clear()
            # Отправка уведомлений
            order_created(order.id)
            admin_notification(order.id)
            return render(request,
                          'thanks.html',
                          {'order': order})
    else:
        form = OrderForm()
    return render(request,
                  'checkout.html',
                  {'cart': cart, 'form': form, 'categories':Category.objects.all()})

