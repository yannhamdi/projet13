from django.core.management.base import BaseCommand
from django.conf import settings

from movies.models import Category, Actor, Movie
from movies.import_api import get_json


class Command(BaseCommand):
    """personnalized command"""
    help = "commands to fill up our database"

    def handle(self, *args, **options):
        """ funcion that will call all the methods to fill our database"""
        self.delete_all()
        self.saving_cat()
    def checking_blank(self, element):
        """ method that check blank lines"""
        keys = ["id_code", "movie_title", "run_time", "movie_released",
                "image_movie", "plot", 'genres', "cast"]
        for key in keys:
            if key not in element or not element[key]:
                return False
        return True

    def saving_category(self, genre):
        Category.objects.get_or_create(cat=genre)

    def saving_actor(self, actor):
        """saving actors"""
        Actor.objects.get_or_create(act=actor)

    def saving_cat(self):
        """methods that fills the db"""
        self.db_movie = get_json()
        for element in self.db_movie:
            movie, created = Movie.objects.get_or_create(
                        id_code=element["id_code"],
                        movie_title=element["movie_title"],
                        run_time=element["run_time"],
                        image_movie=element["image_movie"],
                        plot=element["plot"],
                        movie_released=element["movie_released"])
            papa = (element["genres"])
            for i in range(0, (len(papa))):
                p = (papa[i]).lower()
                self.saving_category(p)
                s = Category.objects.get(cat=p)
                movie.category.add(s)
                movie.save()
                person = ((element["cast"]).split(","))
            for pers in person:
                t = pers.strip()
                self.saving_actor(t)
                u = Actor.objects.get(act=t)
                movie.actor.add(u)
                movie.save()
        
    def delete_all(self):
        Movie.objects.all().delete()
        Category.objects.all().delete()
        Actor.objects.all().delete()
