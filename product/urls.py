from django.urls import path
from .views import main_page, category_view, product_view,catalog

urlpatterns = [
    path('category/<slug>/', category_view, name='category_detail'),
    path('<int:id>/<slug:slug>/', product_view, name='product'),
    path('catalog/', catalog, name='catalog'),
    path('', main_page, name = 'main'),
    
]
