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
    #comment = models.TextField('Комментарий', max_length=300)
    created_date = models.DateTimeField('Дата создания',auto_now_add=True)
    updated = models.DateTimeField('Изменено',auto_now=True)
    paid = models.BooleanField('Оплачено',default=False)
   

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural='Заказы'
        ordering = ['-created_date']

         
    def __str__(self):
        return 'Order {}'.format(self.id)
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE,verbose_name='Товары')
    price = models.DecimalField('Цена',max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество',default=1)


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural='Товары'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity