from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from users.models.user import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=10, unique=True, validators=[MinLengthValidator(5)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=255, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, related_name='ads', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='pictures/%Y/%m/%d', null=True, blank=True)
    is_published = models.BooleanField(default=False)
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
