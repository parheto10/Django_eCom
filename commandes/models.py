# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import math
from django.db import models
from billing.models import BillingProfile
from django.db.models.signals import pre_save, post_save
from cfe_eCommerce.utils import unique_cmde_id_generator
from paniers.models import Panier

CMDE_STATUS_CHOIX = (
    ('nouvelle', 'Nouvelle'),
    ('payer', 'Payer'),
    ('expédie', 'Expédie'),
    ('rembourse', 'Rembourse'),
)


class CommandeManager(models.Manager):
    def new_or_get(self, billing_profile, panier_obj):
        created = False
        qs = self.get_queryset().filter(
            billing_profile=billing_profile,
            panier=panier_obj,
            active=True
        )
        if qs.count() == 1:
            obj = qs.first()
        else:
            obj = self.model.objects.create(
                billing_profile=billing_profile,
                panier=panier_obj
            )
            created = True
        return obj, created

class Commande(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, null=True, blank=True)
    cmde_id   = models.CharField(max_length=150, blank=True)
    panier      = models.ForeignKey(Panier)
    status      = models.CharField(max_length=250, default='nouvelle', choices=CMDE_STATUS_CHOIX)
    livraison = models.DecimalField(default=1000.00, max_digits=100, decimal_places=2)
    total_cmde  = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    active      = models.BooleanField(default=True)

    def __unicode__(self):
        return self.cmde_id

    objects = CommandeManager()

    def maj_total(self):
        total_panier = self.panier.total
        total_livraison = self.livraison
        new_total_cmde = math.fsum([total_panier, total_livraison])
        formatted_total = format(new_total_cmde, '.2f')
        self.total_cmde = formatted_total
        self.save()
        return new_total_cmde


def pre_save_create_cmde_id(sender, instance, *args, **kwargs):
    if not instance.cmde_id:
        instance.cmde_id = unique_cmde_id_generator(instance)
    qs = Commande.objects.filter(panier=instance.panier).exclude(
        billing_profile=instance.billing_profile
    )
    if qs.exists():
        qs.update(active=False)
pre_save.connect(pre_save_create_cmde_id, sender=Commande)


def post_save_panier_total(sender, created, instance, *args, **kwargs):
    if not created:
        panier_obj = instance
        total_panier = panier_obj.total
        panier_id = panier_obj.id
        qs = Commande.objects.filter(panier__id=panier_id)
        if qs.count() == 1:
            cmde_obj = qs.first()
            cmde_obj.maj_total()

post_save.connect(post_save_panier_total, sender=Panier)

def post_save_cmde(sender, instance, created, *args, **kwargs):
    print("traitement")
    if created:
        print("maj....effectuée")
        instance.maj_total()

post_save.connect(post_save_cmde, sender=Commande)

#genere l'identifiant de la Commande?
#genere le total de la Commande?

# Create your models here.
