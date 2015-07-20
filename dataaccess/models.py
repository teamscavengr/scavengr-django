from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    profile_pic = models.URLField(blank=True, null=True)


class Place(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True,null=True)
    email = models.EmailField(blank=True, null=True)

