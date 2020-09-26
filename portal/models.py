from django.db import models
from django.db.models import Model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings
from django.contrib import admin

from django.core.mail import send_mail

class Service(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    servicedate = models.DateField()

    vehiclenum = models.TextField(max_length=100, blank=True)

    manufacturer = models.TextField(max_length=100, blank=True)

    stype = models.TextField(max_length=100, blank=True)

    status = models.TextField(max_length=30, default="Scheduled")

    completed = models.BooleanField(default=False)

    readytodeliver = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        if self.readytodeliver == False:
            super(Service, self).save(*args, **kwargs)

        else:
            
            message = "Hello "+self.user.get_full_name()+", We are pleased to inform you that the Bike service for "+self.vehiclenum+" has been completed and it's Ready for Pickup."
            send_mail('Bike Service Completed', message, 'johnbikeservice@gmail.com', [self.user.email], fail_silently=False)
            super(Service, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.vehiclenum + " " + self.user.get_full_name()}'
    


       


class Servicetype(models.Model):

    name = models.TextField(max_length=30, blank=True)

    stype = models.TextField(max_length=100, blank=True)

    description = models.TextField(max_length=500, blank=True)

    onhold = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'