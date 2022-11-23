from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class WatchlistItem(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=50)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    release_date = models.CharField(max_length=20)
    review = models.CharField(max_length=60)