from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q
from product.models import Product
from .forms import SearchForm

# Create your views here.
def search_view(request):

    template = 'search_result.html'
    search_product = Product.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        q = Q(name__icontains=keyword)
        search_product = search_product.filter(q)
    else:
        keyword =''
   
    
    return render(request,template, {'search_product':search_product})