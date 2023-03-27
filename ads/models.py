from django.db import models


class ADS(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=50)
    price = models.IntegerField(null=False)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=255)
    is_published = models.BooleanField(default=False)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
