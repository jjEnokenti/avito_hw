from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ad(models.Model):
    name = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=False)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='media/%d/%m/%Y', null=True, blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name
