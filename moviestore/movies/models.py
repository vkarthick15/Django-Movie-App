from platform import release
from re import template
from django.db import models
from matplotlib.pyplot import title
from numpy import generic

# Create your models here.

class movies(models.Model):
    title = models.CharField(max_length=256)
    imdbRating = models.FloatField(default=0)
    posterurl = models.CharField(max_length=256,null=True)
    storyline = models.TextField(null=True)
    releaseDate = models.CharField(max_length=256,null=True)
    duration = models.CharField(max_length=256,null=True)
    year = models.CharField(max_length=256,null=True)

    def __str__(self):
        return f"{self.id} {self.title}"

class Review(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(movies, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Review {self.id}"
