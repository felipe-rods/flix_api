from django.db import models


COUNTRY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('SPAIN', 'Espanha'),
    ('FRANCE', 'França'),
    ('MEXICO', 'México'),
    ('ARGENTINA', 'Argentina')
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(blank=True, null=True)
    country = models.CharField(
        max_length=100,
        choices=COUNTRY_CHOICES,
        blank=True,
        null=True
        )
    
    def __str__(self):
        return self.name
