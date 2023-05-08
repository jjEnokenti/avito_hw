from django.db import models

from ads.models import Ad
from users.models.user import User


class Selection(models.Model):
    name = models.CharField(max_length=155, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'
        ordering = ['owner']
