from django.urls import path
from django.conf.urls import url
from .views import cart_detail,cart_add,cart_remove

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<slug>/', cart_add, name='cart_add'),
    path('remove/<slug>/', cart_remove, name = 'cart_remove'),
    
]
