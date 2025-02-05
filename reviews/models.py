from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from movies.models import Movie


class Review(models.Model):
    movie = models.ForeignKey(
        Movie,
        on_delete=models.PROTECT,
        related_name='reviews'
    )
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, 'Rating cannot be lower than 1.'),
            MaxValueValidator(5, 'Rating cannot be higher than 5.')
        ]
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.movie
