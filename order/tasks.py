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
    message = f' Добрый день,{order.name}!\n\nВаш заказ успешно принят.\
                  Номер вашего заказа {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'info@mail.ru',
                          [order.email])
    return mail_sent