from django.core.exceptions import ValidationError


def capital_letter_validator(value):
    first_letter = value[0]
    if not first_letter.isupper():
        raise ValidationError('Your name must start with a capital letter!')


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')
