from django.db import models

# Create your models here.
class WatchlistItem(models.Model):
    watched = models.CharField(max_length=5)
    title = models.CharField(max_length=50)
    rating = models.FloatField()
    release_date = models.CharField(max_length=20)
    review = models.CharField(max_length=60)