from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    '''
     Модель категории товаров
    '''
    name =  models.CharField('Название',max_length=120,db_index=True)
    slug = models.SlugField('URL', max_length=120,unique=True)
    title =  models.CharField('Title',max_length=100,blank=True)
    description_seo =  models.CharField('Description',max_length=140,blank=True)

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

class Product(models.Model):
    '''
        Модель товара
    '''
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField('Цена со скидкой',max_digits=10, decimal_places=2, blank=True, null=True)
    sale = models.IntegerField('Скидка в процентах', blank=True, null=True,default=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name='Товар'
        verbose_name_plural='Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('product_view',
                           args=[self.id, self.slug])
                           
    def get_sale(self):
        '''Расчитать стоимость со скидкой'''
        discount_price = int(self.discount_price * (100 - self.sale) / 100)
        return discount_price



