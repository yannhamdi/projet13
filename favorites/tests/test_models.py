from django.test import TestCase
from favorites.models import Favorite
from users.models import User
from movies.models import Category, Movie, Actor



class TestFavoriteModel(TestCase):
    def test_favorite_model(self):
        category = Category.objects.get_or_create(cat= "drama")
        actor = Actor.objects.get_or_create(act="bruce willis")
        movie_1, created = Movie.objects.get_or_create(id_code=20930393, movie_title="die hard", movie_released="2005",
                                             run_time="105", image_movie="www.film.fr", plot="story of terrorism")
        s = Category.objects.get(cat="drama")
        movie_1.category.add(s)
        movie_1.save()
        a = Actor.objects.get(act="bruce willis")
        movie_1.actor.add(a)
        movie_1.save(())
        user_1 , created = User.objects.get_or_create(username="yann80", last_name="hamdi", first_name="yann", email= "hamdiyann@hotmail.com", password="ch171283")
        favoris, created = Favorite.objects.get_or_create(user_link=user_1, movie_saved=movie_1)
        self.assertEqual(favoris.user_link, user_1)
        self.assertEqual(favoris.movie_saved, movie_1)

