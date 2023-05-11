from rest_framework import serializers


class IsPublishedNotTrue:
    def __call__(self, value):
        if value is True:
            raise serializers.ValidationError('Нельзя публиковать только что созданное объявление.')
