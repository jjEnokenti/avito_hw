from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField(null=False)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=255)
    is_published = models.BooleanField(default=True)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
