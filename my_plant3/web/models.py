from django.core.validators import MinLengthValidator
from django.db import models

from my_plant3.web.validators import capital_letter_validator, only_letters_validator


class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=(
            MinLengthValidator(2),
        ),
    )
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            capital_letter_validator,
        ),
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            capital_letter_validator,
        ),
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Plant(models.Model):
    PLANT_TYPES = (
        ('Outdoor Plants', 'Outdoor Plants'),
        ('Indoor Plants', 'Indoor Plants'),
    )

    plant_type = models.CharField(
        null=False,
        blank=False,
        max_length=14,
        choices=PLANT_TYPES,
    )
    name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(
            MinLengthValidator(2),
            only_letters_validator,
        ),
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
    )
