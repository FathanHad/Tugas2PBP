from django.db import models

# Create your models here.
class WatchlistMovies(models.Model):
    is_watched = models.CharField(max_length=10)
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()