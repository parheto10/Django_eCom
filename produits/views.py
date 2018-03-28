# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.urls import reverse

from .models import Produit

class ProduitFeaturedListView(ListView):
    template_name = "produits/produit_list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Produit.objects.all().featured()

class ProduitFeaturedDetailView(DetailView):
    queryset = Produit.objects.featured()
    template_name = "produits/featured_detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     #request = self.request
    #     return Produit.objects.featured()

class ProduitListView(ListView):
    #queryset = Produit.objects.all()
    template_name = "produits/produit_list.html"
    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProduitListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Produit.objects.all()


def produits(request):
    queryset = Produit.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, 'produits/list.html', context)


class ProduitDetailSlugView(DetailView):
    queryset = Produit.objects.all()
    template_name = "produits/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        #produit = get_object_or_404(Produit, slug=slug, active=True)
        try:
            produit = get_object_or_404(Produit, slug=slug, active=True)
        except Produit.MultipleObjectsReturned:
            qs = Produit.objects.filter(slug=slug, active=True)
            produit = qs.first()
        except :
            raise Http404('Warning !!')
        return produit



class ProduitDetailView(DetailView):
    #queryset = Produit.objects.all()
    template_name = "produits/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        produit = Produit.objects.get_by_id(pk)
        if produit is None:
            raise Http404("Aucun produit avec cet Identifiant")
        return produit

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Produit.objects.filter(pk=pk)

def detail(request, pk=None, *args, **kwargs):
    #produit = Produit.objects.get(pk=pk, featured=True)
    #produit = get_object_or_404(Produit, pk=pk)
    # try:
    #     produit = Produit.objects.get(id=pk)
    # except Produit.DoesNotExist:
    #     print("Article introuvable sur notre Site")
    #     raise Http404("Aucun produit avec cet Identifiant")
    # except:
    #     print("Huuu?")
    produit = Produit.objects.get_by_id(pk)
    if produit is None:
        raise Http404("Aucun produit avec cet Identifiant")
    # print(produit)
    # qs = Produit.objects.filter(id=pk)
    # # print(qs)
    # if qs.exists and qs.count() == 1: #long(de la requete qs)
    #     produit = qs.first()
    # else:
    #     raise Http404("Aucun produit avec cet Identifiant")
    context = {
        'object' : produit,
    }
    return render(request, 'produits/detail.html', context)



# Create your views here.
