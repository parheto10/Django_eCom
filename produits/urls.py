from django.conf.urls import url

#from .views import home, about, contact, login_page, insription
from produits.views import (
    ProduitListView,
    produits,
    ProduitDetailView,
    ProduitDetailSlugView,
    #detail,
    #ProduitFeaturedListView,
    #ProduitFeaturedDetailView,
)

urlpatterns = [
    #Liste des produits
    #url(r'^$', produits, name='produits'),
    url(r'^$', ProduitListView.as_view(), name='produits'),
    #detail produit
    url(r'^(?P<slug>[\w-]+)/$', ProduitDetailSlugView.as_view(), name='detail'),

]

# #featured produit url
    # url(r'^featured/$', ProduitFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$', ProduitFeaturedDetailView),

    # #featured produit url
    # url(r'^produits_cbv/$', ProduitListView.as_view(), name='produits'),
    # url(r'^produits_fbv/$', produits, name='produits'),
    #
    # #detail url
    # #url(r'^produits_cbv/(?P<pk>\d+)/$', ProduitDetailView.as_view(), name='detail'),
    # url(r'^produits_cbv/(?P<slug>[\w-]+)/$', ProduitDetailSlugView.as_view(), name='detail'),
    # url(r'^produits_fbv/(?P<pk>\d+)/$', detail, name='detail'),
    # url(r'^produits_fbv/(?P<slug>[\w-]+)/$', detail, name='detail'),
