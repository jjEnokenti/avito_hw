from datetime import date, timedelta

from django.core.exceptions import ValidationError


def age_validation(value: date):
    age = date.today() - value
    if age < timedelta(days=365*9):
        raise ValidationError('Вам должны быть больше 9 лет, чтобы зарегистрироваться.')


def email_validation(value: str):
    if value.endswith('rumbler.ru'):
        raise ValidationError('Регистрация с почтовым адресом на домене rumbler.ru запрещена.')
