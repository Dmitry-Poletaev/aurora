from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, View
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models.functions import Coalesce
from cart.forms import CartAddProductForm




# Create your views here.
def main_page(request):
    categories = Category.objects.all()
    
    return render(request, 'index.html',{'categories':categories})

def category_view(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()

        # Пагинация
    paginator = Paginator(products,20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
    'category': category,
    'products':products,
    'categories': categories
    }
    return render(request, 'category.html', context)


def product_view(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request,'product.html',{'product':product,'categories':categories,
                                        'cart_product_form': cart_product_form})
    

def catalog(request):
    categories = Category.objects.all()
    products = Product.objects.all()

        # Пагинация
    paginator = Paginator(products,20)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    context = {
    'products':products,
    'categories': categories
    }
    return render(request, 'catalog.html', context)