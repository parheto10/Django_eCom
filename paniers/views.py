# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from produits.models import Produit
from .models import Panier

# def cree_panier(user=None):
#     panier_obj = Panier.objects.create(user=None)
#     print('Ajouter Nouveau Panier')
#     return panier_obj

def panier_home(request):
    panier_obj, new_obj = Panier.objects.new_or_get(request)
    # produits = panier_obj.produits.all()
    # total = 0
    # for x in produits:
    #     total += x.prix
    # print(total)
    # panier_obj.total = total
    # panier_obj.save()
    context = {
        "panier" : panier_obj,
    }
    return render(request, 'paniers/home.html', context)

def maj_panier(request):
    #print(request.POST)
    produit_id = request.POST.get('produit_id')
    if produit_id is not None:
        try:
            produit_obj = Produit.objects.get(id=produit_id)
        except Produit.DoesNotExist:
            print('Afficher le Message Suivant, Article terminer!!')
            return redirect('panier:panier')
        panier_obj, new_obj = Panier.objects.new_or_get(request)
        if produit_obj in panier_obj.produits.all():
            panier_obj.produits.remove(produit_obj)
        else:
            panier_obj.produits.add(produit_obj)
        request.session['panier_items'] = panier_obj.produits.count()
        #return redirect(produit_obj.get_absolute_url())
    return redirect('panier:panier')



# Create your views here.
