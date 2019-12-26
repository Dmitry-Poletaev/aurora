"""auroraonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from information.sitemaps import ProductSitemap, CategorySitemap, InformationSitemap

sitemaps = {
    'product': ProductSitemap,
    'category': CategorySitemap,
    'information': InformationSitemap,
}


handler404 = 'information.views.handler404'
#handler500 = 'information.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap,{'sitemaps': sitemaps}),
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt',content_type='text/plain')),
    path('checkout/',include('order.urls', namespace='orders')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('product.urls')),
    path('', include('search.urls')),
    path('',include('information.urls')),
    path('captcha/',include('captcha.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)