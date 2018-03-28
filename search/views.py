# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from produits.models import Produit

class SearchProduitView(ListView):
    template_name = "search/vue.html"
    def get_context_data(self,*args, **kwargs):
        context = super(SearchProduitView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context
    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q', None)
        print (query)
        if query is not None:
            return Produit.objects.filter(titre__icontains=query)
        return Produit.objects.featured()
    '''
    __icontains = Tous attribut contenant la valeur entree
     __iexact = Tous attribut ayant la valeur entree
    '''

# Create your views here.
