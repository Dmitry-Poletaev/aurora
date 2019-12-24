from django.shortcuts import render
from product.models import Category
from django.shortcuts import render_to_response


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

def handler404(request, exception, template_name="404.html"):
    response = render_to_response("404.html")
    response.status_code = 404
    return response

def handler500(request, exception, template_name="500.html"):
    response = render_to_response("500.html")
    response.status_code = 500
    return response

