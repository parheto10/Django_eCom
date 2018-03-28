# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Produit

class ProduitAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'slug', ]
    class Meta:
        model = Produit

admin.site.register(Produit, ProduitAdmin)

# Register your models here.
