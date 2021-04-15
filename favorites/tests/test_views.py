from django.test import TestCase
from django.urls import reverse
from django.core.paginator import Paginator
from favorites.models import Favorite
from movies.models import Category, Movie, Actor
from users.models import User

class FavoriteView(TestCase):

    def setUp(self):
        self.category = Category.objects.get_or_create(cat= "drama")
        self.acotr = Actor.objects.get_or_create(act= "bruce willis")
        self.movie_1, created = Movie.objects.get_or_create(id_code=20930393, movie_title="die hard", movie_released="2005",
                                        run_time="105", image_movie="www.film.fr", plot="story of terrorism")
        s = Category.objects.get(cat="drama")
        self.movie_1.category.add(s)
        self.movie_1.save()
        a = Actor.objects.get(act="bruce willis")
        self.movie_1.actor.add(a)
        self.movie_1.save(())
        self.movie_2, created = Movie.objects.get_or_create(id_code=20930390, movie_title="platoon", movie_released="1999",
                                        run_time="240", image_movie="www.platoon.fr", plot="story of war")
        self.movie_2.category.add(s)
        self.movie_2.save()
        self.movie_2.actor.add(a)
        self.movie_2.save()
        self.user_1 , created = User.objects.get_or_create(username="yann80", last_name="hamdi", first_name="yann", email= "hamdiyann@hotmail.com", password="ch171283")


    def test_response_post(self):
        self.client.force_login(self.user_1)
        response = self.client.get(reverse('saving_search', args=[self.movie_1.id_code]))
        self.assertEqual(response.status_code, 302)

    def test_display_account(self):
        # Create 13 search for pagination
        self.client.force_login(self.user_1)
        response = self.client.get(reverse('display_account'))
        fav_1, created = Favorite.objects.get_or_create(user_link=response.context.get('user'),movie_saved=Movie.objects.get(id_code=20930393))
        fav_2, created = Favorite.objects.get_or_create(user_link=response.context.get('user'),movie_saved=Movie.objects.get(id_code=20930390))
        
        new_response = self.client.get(reverse('display_account'))
        self.assertEqual(new_response.status_code, 200)
        self.favoris_list = Favorite.objects.all()
        self.assertTrue('page_obj' in new_response.context)
        self.assertTrue(len(self.favoris_list) == 2)
        response_2 = self.client.get(reverse('display_account')+'?page=2')
        self.assertEqual(response_2.status_code, 200)
        self.assertTrue('page_obj' in response.context)
        
       
   
