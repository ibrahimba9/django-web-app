from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MaxLengthValidator,
)
from django.db import models


class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = "HH"
        SYNTH_POP = "SP"
        ALTERNATIVE_ROCK = "AR"
        METAL = "M"
        RHYTHM_N_BLUES = "RNB"

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Listing(models.Model):
    class ListingType(models.Choices):
        RECORDS = "records"
        CLOTHING = "clothing"
        POSTERS = "posters"
        Miscellaneous = "miscellaneous"

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1900), MaxLengthValidator(2023)],
    )
    type = models.fields.CharField(choices=ListingType.choices, max_length=20)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title}"
