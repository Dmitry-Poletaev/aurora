from django.urls import path
from .views import main_page, category_view, product_view

urlpatterns = [
    path('category/<slug>/', category_view, name='category_detail'),
    path('product/<slug>/', product_view, name='product'),
    path('', main_page, name = 'main'),
    
]
