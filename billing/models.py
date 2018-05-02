# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from comptes.models import InviteEmail

User = settings.AUTH_USER_MODEL

class BilingProfileManager(models.Manager):
    def new_or_get(self, request):
        user = request.user
        invite_email_id = request.session.get('new_invite_id')
        created = False
        obj = None
        if user.is_authenticated:
            'Verification comme Utilisateur'
            obj, created = self.model.objects.get_or_create(
                user=user,
                email=user.email
            )
        elif invite_email_id is not None:
            'Verification comme Invite'
            invite_email_obj = InviteEmail.objects.get(id=invite_email_id)
            obj, created = self.model.objects.get_or_create(
                email=invite_email_obj.email
            )
        else:
            pass

        return obj, created

class BillingProfile(models.Model):
    user        = models.OneToOneField(User, null=True, blank=True)
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    object = BilingProfileManager()

    def __unicode__(self):
        return self.email

#
# def billing_profile_created_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         print("Send To Strip/Braintree")
#         instance.client_Id = newID
#         instance.save()
# post_save.connect(billing_profile_created_receiver, sender=User)

def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)
post_save.connect(user_created_receiver, sender=User)


# Create your models here.
