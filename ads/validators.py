from django.core.exceptions import ValidationError


def is_published_cant_be_true(value: bool):
    if value is True:
        raise ValidationError(f'Field is_published can\'t be True.')
