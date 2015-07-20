from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    profile_pic = models.URLField(blank=True, null=True)


class Place(models.Model):
    name = models.CharField(max_length=100,blank=True)
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True,null=True)
    email = models.EmailField(blank=True, null=True)
    longitude = models.DecimalField (max_digits=9, decimal_places=6,blank=True, null=True)
    latitude = models.DecimalField (max_digits=9, decimal_places=6,blank=True, null=True)
    owner =  models.ForeignKey('auth.User', related_name='places')

