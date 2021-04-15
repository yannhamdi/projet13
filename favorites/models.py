from django.db import models
from django.conf import settings


class Favorite(models.Model):
    """class that create a model favoris that will connect
    the user's model and the products' model"""
    user_link = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  related_name="user_favoris")
    movie_saved = models.ForeignKey("movies.Movie",
                                         on_delete=models.CASCADE,
                                         related_name="user_search")
   
