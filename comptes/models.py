# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class InviteEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.email

# Create your models here.
