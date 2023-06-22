from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def validate_string_starts_with_capital_letter(value):
    first_char = value[:1]

    if not first_char.isupper():
        raise ValidationError('Your name must start with a capital letter!')


def validate_string_contains_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Plant name should contain only letters!')


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 10
    MIN_USERNAME_LENGTH = 2
    MAX_FIRST_NAME_LENGTH = 20
    MAX_LAST_NAME_LENGTH = 20

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            validators.MinValueValidator(MIN_USERNAME_LENGTH),
        ],
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=[
            validate_string_starts_with_capital_letter,
        ],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=[
            validate_string_starts_with_capital_letter,
        ],
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Plant(models.Model):
    MAX_TYPE_LENGTH = 14
    MAX_NAME_LENGTH = 20
    MIN_NAME_LENGTH = 2

    OUTDOOR = 'Outdoor Plants'
    INDOOR = 'Indoor Plants'

    TYPES = (
        (OUTDOOR, OUTDOOR),
        (INDOOR, INDOOR),
    )

    plant_type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        choices=TYPES,
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=[
            validators.MinValueValidator(MIN_NAME_LENGTH),
            validate_string_contains_only_letters,
        ],
        null=False,
        blank=False,

    )

    image_URL = models.URLField(
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
