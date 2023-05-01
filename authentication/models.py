from django.db import models
from django.contrib.auth.models import AbstractUser


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
