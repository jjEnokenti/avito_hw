from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=255, null=False)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=False)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='media/%d/%m/%Y')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20, unique=True, blank=False)
    password = models.CharField(max_length=100, blank=False)
    role = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    locations = models.ManyToManyField('Location')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Location(models.Model):
    name = models.CharField(max_length=155, unique=True)
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
