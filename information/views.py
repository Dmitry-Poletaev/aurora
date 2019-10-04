from django.shortcuts import render
from product.models import Category

# Create your views here.
def about(request):
    return render(request,'about.html',{'categories':Category.objects.all()})


def service(request):
    return render(request,'service.html',{'categories':Category.objects.all()})


def politic_conf(request):
    return render(request,'politic_conf.html',{'categories':Category.objects.all()})

def warranty(request):
    return render(request,'warranty.html',{'categories':Category.objects.all()})

def credit(request):
    return render(request,'credit.html',{'categories':Category.objects.all()})

def contact(request):
    return render(request,'contact.html',{'categories':Category.objects.all()})


