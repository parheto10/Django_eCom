"""cfe_eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from paniers.views import panier_home
from .views import home, about, contact, login_page, insription
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/$', login_page, name='login'),
    url(r'^insription/$', insription, name='insription'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact'),
    #url(r'^panier/$', panier_home, name='panier'),
    url(r'^panier/', include('paniers.urls', namespace="panier", app_name="panier")),
    url(r'^bootstrap/$', TemplateView.as_view(template_name='bootstrap/example.html'), name='bootstrap'),

    #url relative au produits
    url(r'^produits/', include('produits.urls', namespace="produits", app_name="produits")),
    url(r'^search/', include('search.urls', namespace="search", app_name="search")),
    url(r'^admin/', admin.site.urls),
]#
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)