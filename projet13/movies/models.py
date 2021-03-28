"""create models for database"""
from django.db import models
from .managers import ProductManager


class Category(models.Model):
    """we create the name for each categories"""
    cat = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.cat

class Actor(models.Model):
    """we create the name for each categories"""
    act = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.act

class Movie(models.Model):
    """ we class the model for each products"""
    id_code = models.BigIntegerField(primary_key=True)
    movie_title = models.CharField(max_length=255)
    movie_released = models.CharField(max_length=50)
    run_time = models.CharField(max_length=50)
    image_movie = models.URLField(max_length=255)
    plot = models.TextField()
    category = models.ManyToManyField("Category", related_name="movies")
    actor = models.ManyToManyField("Actor", related_name="movie")

    def __str__(self):
        return self.movie_title

    objects = ProductManager()
        