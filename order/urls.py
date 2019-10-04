from django.urls import path
from .views import checkout_view,thanks


urlpatterns =[
    path('', checkout_view, name='checkout'),
    path('thanks/', thanks, name='thanks'),
]