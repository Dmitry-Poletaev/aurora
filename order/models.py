from django.db import models
from django.conf import settings
from product.models import Product

# Create your models here.




class Order(models.Model):
    """
    Модель заказа
    """
    name =  models.CharField('Имя',max_length=50)
    last_name = models.CharField('Фамилия',max_length=50)
    phone = models.CharField('Телефон',max_length=50)
    email = models.EmailField("E-mail", max_length=50)
    comment = models.TextField('Комментарий', max_length=300)
    created_date = models.DateTimeField('Дата создания',auto_now_add=True)
   

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural='Заказы'

         
    def __str__(self):
        return str(self.name)

