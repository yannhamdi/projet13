from django.core.management.base import BaseCommand


from movies.models import Category, Actor, Movie
from movies.imdb_api import imdb_api
import imdb


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
        self.movie_title = []
        self.dbmov = imdb_api()
        self.ia = imdb.IMDb()
        print(self.dbmov)
        self.movies_id = []
        self.movies_results = []
        self.movies_details = {}
        for name in self.dbmov:
            self.movie_title.append(name)
        self.movie_title = set(self.movie_title)
        self.movie_title = list(self.movie_title)
        for title in self.movie_title:
            try:
                search = self.ia.search_movie(title)
                self.movies_id.append(search[0].movieID)
            except Exception as e:
                print("error: %s" % e)
        for id_movie in self.movies_id:
            search_details = self.ia.get_movie(id_movie)
            try:
                self.movies_details['id_code'] = id_movie
                self.movies_details['movie_title'] = search_details['title']
                self.movies_details['run_time'] = search_details['runtimes']
                self.movies_details['movie_released'] = search_details['year']
                self.movies_details['image_movie'] = search_details['cover url']
                self.movies_details['plot'] = search_details['plot'][0]
                self.movies_details['genres'] = search_details['genres']
                self.movies_details['cast'] = str((search_details['cast'][0]))
                self.movies_details['cast'] += ", " + str((search_details['cast'][1]))

                self.movies_results.append(self.movies_details)
                self.movies_details = {}

            except Exception as e:
                print("notre resultat")
                print(len(self.movies_results))
                print(id_movie)
                print("error: %s" % e)
                continue
        self.movies_id = []
        self.movie_title = []
        for element in self.movies_results:
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
