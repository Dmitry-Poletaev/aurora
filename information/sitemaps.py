from django.contrib.sitemaps  import Sitemap
from django.urls import reverse
from product.models import Category, Product


class ProductSitemap(Sitemap):

    def items(self):
        return Product.objects.all()


class CategorySitemap(Sitemap):

    def items(self):
        return Category.objects.all()

class InformationSitemap(Sitemap):

    def items(self):
        return ['about',
        'service',
        'politic_conf',
        'warranty',
        'credit',
        'contact']

    def location(self, item):
        return reverse(item)