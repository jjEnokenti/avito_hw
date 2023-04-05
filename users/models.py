from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=155, unique=True)
    lat = models.FloatField()
    lng = models.DecimalField(max_digits=8, decimal_places=6)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class User(models.Model):
    choices = (('member', 'Пользователь'),
               ('moderator', 'Модератор'),
               ('admin', 'Админ'))

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)
    role = models.CharField(choices=choices, default='member', max_length=9)
    age = models.PositiveIntegerField()
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
