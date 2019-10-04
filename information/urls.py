from django.urls import path
from .views import about, service,politic_conf,warranty, credit,contact


urlpatterns =[
    path('about/',about, name="about"),
    path('service/',service, name="service"),
    path('politika-konfidentsialnosti/',politic_conf,name="politic_conf"),
    path('warranty/',warranty, name="warranty"),
    path('rassrochka/',credit, name="credit"),
    path('contact/',contact, name="contact"),
]