from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(User, related_name='ads', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=False)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='pictures/%Y/%m/%d', null=True, blank=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    @property
    def category_name(self):
        return self.category.name if self.category else None

    @property
    def author_name(self):
        return self.author.username if self.author else None

    def __str__(self):
        return self.name
