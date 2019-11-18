from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Отправка e-mail уведомления при успешном выполнении заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Заказ №{order.id}.'
    message = 'Добрый день, {},\n\nВаш заказ успешно оформлен.\
                  Номер вашего заказа {}.'.format(order.name,
                                            order.id)
    mail_sent = send_mail(subject,
                          message,
                          'd.poletaev@vorteil-technology.ru',
                          [order.email])
    return mail_sent