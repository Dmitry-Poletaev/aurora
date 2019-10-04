from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import View

# Create your views here.
def checkout_view(request):
    form = OrderForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thanks/')
        
    return render(request, 'checkout.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')