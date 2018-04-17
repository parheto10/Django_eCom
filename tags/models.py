# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from produits.models import Produit
from produits.utils import unique_slug_generator


class Tag(models.Model):
    titre       = models.CharField(max_length=150)
    slug        = models.SlugField()
    timestamp   = models.DateTimeField(auto_now_add=True)
    active      = models.BooleanField(default=True)
    produits    = models.ManyToManyField(Produit, blank=True)

    def __unicode__(self):
        return self.titre

def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(tag_pre_save_receiver, sender=Tag)



# Create your models here.
