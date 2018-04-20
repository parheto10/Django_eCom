# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import os
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from django.urls import reverse

from .utils import unique_slug_generator

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "produits/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

class ProduitQueryset(models.query.QuerySet):
    def featured(self):
        return self.filter(featured = True, active = True)

    def active(self):
        return self.filter(active = True)

    def search(self, query):
        lookups = (
                Q(titre__icontains=query) |
                Q(description__icontains=query) |
                Q(prix__icontains=query) |
                Q(tag__titre__icontains=query)
        )
        return self.filter(lookups).distinct()

class ProduitManager(models.Manager):
    def get_queryset(self):
        return ProduitQueryset(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self): #Produit.object.featured()
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)

class Produit(models.Model):
    titre           = models.CharField(max_length=255)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    prix            = models.DecimalField(decimal_places=2, max_digits=10, default=39.00)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    objects = ProduitManager()

    def __unicode__(self): #python2
        return self.titre

    def __str__(self): #python3
        return self.titre

    @property
    def nom(self):
        return self.titre

    def get_absolute_url(self):
        #return "/produits/{slug}/".format(slug=self.slug)
        return reverse("produits:detail", kwargs={"slug":self.slug})

def produit_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(produit_pre_save_receiver, sender=Produit)


# Create your models here.
