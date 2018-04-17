# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Panier

# def cree_panier(user=None):
#     panier_obj = Panier.objects.create(user=None)
#     print('Ajouter Nouveau Panier')
#     return panier_obj

def panier_home(request):
    panier_obj, new_obj = Panier.objects.new_or_get(request)
    produits = panier_obj.produits.all()
    total = 0
    for x in produits:
        total += x.prix
    print(total)
    panier_obj.total = total
    panier_obj.save()
    return render(request, 'paniers/home.html', {})

# Create your views here.
