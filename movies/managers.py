"""managers mmodule for queries"""
from django.db import models


class ProductManager(models.Manager):
    """class that filters movies by title"""
    def search_movie_title(self, search_entry):
        """the method will make a request to look for
        the product searched and the one to substitue"""
        returning_request_user = []
        movie_id_by_title = self.filter(movie_title__icontains=search_entry).order_by('id_code')
        if movie_id_by_title:
            for element in movie_id_by_title:
                return movie_id_by_title
        return None

class ActorManager(models.Manager):
    """class that filters movies by actor"""
    def search_movie_actor(self, search_actor):
        """ the methor will make a request by actor"""
        move_id_by_actor = self.filter(act__icontains=search_actor)
        if move_id_by_actor:
            return move_id_by_actor
        return None


class GenreManager(models.Manager):
    """class that filters movies by category"""
    def search_movie_genre(self, search_genre):
        """the method that will make a request by genre"""
        movie_id_by_genre = self.filter(cat__icontains=search_genre)
        if movie_id_by_genre:
            return movie_id_by_genre
        return None
