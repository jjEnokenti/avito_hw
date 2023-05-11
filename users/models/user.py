from django.contrib.auth.models import AbstractUser
from django.db import models

from .location import Location
from users.models.validators import age_validation, email_validation


class User(AbstractUser):
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLES = [
        (MEMBER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Админ')
    ]

    email = models.EmailField(unique=True, validators=[email_validation])
    role = models.CharField(max_length=9, choices=ROLES, default=MEMBER)
    birth_date = models.DateField(validators=[age_validation])
    age = models.PositiveIntegerField(null=True, blank=True)
    locations = models.ManyToManyField(Location)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    # def save(self, *args, **kwargs):
    #     self.set_password(self.password)
    #
    #     return super().save()
