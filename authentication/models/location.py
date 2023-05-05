from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=155, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, default=0)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True, default=0)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name
