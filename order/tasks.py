from celery import task
from django.core.mail import send_mail
from .models import Order, OrderItem
from product.models import Product
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
import weasyprint
from io import BytesIO
#@task
def order_created(order_id):
    """
    Отправка e-mail уведомления при успешном оформлении заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Заказ №{order.id}.'
    message = 'Добрый день, {},\nВаш заказ успешно оформлен.\
                  \nНомер вашего заказа {}.'.format(order.name, order.id)
                                            
    mail_sent = send_mail(subject,
                          message,
                          'd.poletaev@vorteil-technology.ru',
                          [order.email])
    return mail_sent

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
    mail_sent = email.send()
    return mail_sent
