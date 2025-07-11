from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=32)
    year = models.IntegerField()
    genre = models.CharField(max_length=32)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    running_time = models.PositiveIntegerField()
    content = models.TextField()
    director = models.CharField(max_length=32)
    actors = models.CharField(max_length=200)