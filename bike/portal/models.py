from django.db import models
from django.db.models import Model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.conf import settings

class Service(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    servicedate = models.DateTimeField()

    stype = models.TextField(max_length=100, blank=True)

    status = models.TextField(max_length=30, blank=True)

    completed = models.BooleanField(default=False)

    readytodeliver = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.user.username}'

class Servicetype(models.Model):

    name = models.TextField(max_length=30, blank=True)

    stype = models.TextField(max_length=100, blank=True)

    description = models.TextField(max_length=500, blank=True)

    onhold = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'