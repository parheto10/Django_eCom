from django.conf.urls import url

#from .views import home, about, contact, login_page, insription
from .views import (
    SearchProduitView,
    #ProduitDetailSlugView,
)

urlpatterns = [
    url(r'^$', SearchProduitView.as_view(), name='query'),
]
