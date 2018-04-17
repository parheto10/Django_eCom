# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, m2m_changed

from produits.models import Produit

User = settings.AUTH_USER_MODEL

class PanierManager(models.Manager):

    def new_or_get(self, request):
        panier_id = request.session.get("panier_id", None)
        qs = self.get_queryset().filter(id=panier_id)
        if qs.count() == 1:
            new_obj = False
            panier_obj = qs.first()
            if request.user.is_authenticated() and panier_obj.user is None:
                panier_obj.user = request.user
                panier_obj.save()
        else:
            panier_obj = Panier.objects.new_panier(user=request.user)
            new_obj = True
            request.session['panier_id'] = panier_obj.id
        return panier_obj, new_obj

    def new_panier(self, user=None):
        user_obj  = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)

class Panier(models.Model):
    user         = models.ForeignKey(User, null=True, blank=True)
    produits     = models.ManyToManyField(Produit, blank=True)
    subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total        = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    ajouter_le   = models.DateTimeField(auto_now_add=True)

    objects = PanierManager()

    def __unicode__(self):
        return str(self.id)


def pre_save_panier_receiver(sender, action, instance, *args, **kwargs):
    #print(action)
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        produits = instance.produits.all()
        total = 0
        for x in produits:
            total += x.prix
        instance.subtotal = total
        instance.save()

m2m_changed.connect(pre_save_panier_receiver, sender=Panier.produits.through)

# Create your models here.
