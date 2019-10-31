from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    '''
     Модель категории товаров
    '''
    name =  models.CharField('Название',max_length=120)
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

    name = models.CharField('Название',max_length=120)
    slug = models.SlugField('URL', max_length=255, unique=True)
    image = models.ImageField('Изображение',upload_to='images/', blank=True)
    description = RichTextField('Описание',blank=True)
    price = models.DecimalField('Цена',max_digits=10, decimal_places=2)
    discount_price = models.DecimalField('Цена со скидкой',max_digits=10, decimal_places=2, blank=True, null=True)
    sale = models.IntegerField('Скидка в процентах', blank=True, null=True,default=0)
    created_date = models.DateTimeField('Дата создания',auto_now_add=True)
    available = models.BooleanField('В наличии',default=True,blank=True)
    updated_at = models.DateTimeField('Дата изменения',auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    title =  models.CharField('Title',max_length=100,blank=True)
    description_seo =  models.CharField('Description',max_length=140,blank=True)
    
    



    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'
        ordering = ['price','discount_price']
        index_together = (('id', 'slug'),)
        

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product',  args=[self.id, self.slug])

    def get_sale(self):
        '''Расчитать стоимость со скидкой'''
        discount_price = int(self.discount_price * (100 - self.sale) / 100)
        return discount_price

