from django.conf.urls import url

#from .views import home, about, contact, login_page, insription
from .views import (
   panier_home,
   maj_panier,
   checkout_home
)

urlpatterns = [
    url(r'^$', panier_home, name='panier'),
    url(r'^checkout/$', checkout_home, name='checkout'),
    url(r'^update/$', maj_panier, name='update'),
]
