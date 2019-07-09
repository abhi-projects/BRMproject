from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField()
    publisher = models.CharField(max_length=100)


class BrmUser(models.Model):
    user = models.OneToOneField(User, on_delete='models.CASCADE')
    nick_name = models.CharField(max_length=20, blank=False)
