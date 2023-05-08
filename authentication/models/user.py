from django.contrib.auth.models import AbstractUser
from django.db import models

from .location import Location


class User(AbstractUser):
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLES = [
        (MEMBER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Админ')
    ]

    role = models.CharField(max_length=9, choices=ROLES, default=MEMBER)
    age = models.PositiveIntegerField()
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    # def save(self, *args, **kwargs):
    #     self.set_password(self.password)
    #
    #     return super().save()
