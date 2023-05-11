import datetime

import factory

from ads.models import Category, Ad
from users.models.user import User


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = '1234'
    email = factory.Faker('email')
    birth_date = datetime.datetime.today() - datetime.timedelta(days=365 * 9)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')
    slug = factory.Faker('ean', length=8)


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = factory.Faker('company')
    author = factory.SubFactory(AuthorFactory)
    price = 1000
    category = factory.SubFactory(CategoryFactory)

#
# class SelectionFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Selection
#
#     name = factory.Faker('name')
#     owner = factory.SubFactory(AuthorFactory)
