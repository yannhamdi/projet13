from django.test import TestCase
from django.urls import reverse
from movies.forms import ProductSearch
from movies.views import home, lire, search
from movies.models import Category, Movie, Actor


class MoviesView(TestCase):
    def setUp(self):
        self.category = Category.objects.get_or_create(cat= "drama")
        self.actor = Actor.objects.get_or_create(act="bruce willis")
        self.movie, created = Movie.objects.get_or_create(id_code=20930393, movie_title="die hard", movie_released="2005",
                                run_time="105", image_movie="www.reine.fr", plot="story of guns and terrorism")
        s = Category.objects.get(cat="drama")
        self.movie.category.add(s)
        self.movie.save()
        a = Actor.objects.get(act="bruce willis")
        self.movie.actor.add(a)
        self.movie.save()
        self.category_1 = Category.objects.get_or_create(cat= "drama")
        self.actor_1 = Actor.objects.get_or_create(act="burt lancaster")
        self.movie_1, created = Movie.objects.get_or_create(id_code=20930394, movie_title="hard", movie_released="2006",
                                run_time="98", image_movie="www.film.fr", plot="some random plot")
        s_1 = Category.objects.get(cat="drama")
        self.movie.category.add(s_1)
        self.movie.save()
        a_1 = Actor.objects.get(act="burt lancaster")
        self.movie.actor.add(a_1)
        self.movie.save()
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_display_all(self):
        response = self.client.get(reverse('display_all'))
        self.assertEqual(response.status_code, 200)
    def test_search(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    def test_search(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
    def test_search_with_post(self):
        response_1 = self.client.post(reverse('search'), {'search': 'die hard'} )
        self.assertEqual(response_1.status_code, 200)
    def test_lire(self):
        response = self.client.post(reverse('lire', args=[20930393]))
        self.assertEqual(response.status_code, 200)
    
    def test_lire_error(self):
        response = self.client.post(reverse('lire', args=[2093]))
        self.assertEqual(response.status_code, 404)
    
    def test_search_with_post_error(self):
        response_1 = self.client.post(reverse('search') ,{'search': 'pppp'})
        self.assertEqual(response_1.status_code, 200)

    def test_search_by_category(self):
        # Create 13 search for pagination
        list_movie_cat = Category.objects.search_movie_genre('drama')
        response = self.client.post(reverse('search'),{'search': 'drama'})
        self.list_movie_by_cat = Movie.objects.filter(category__in=list_movie_cat)   
        self.assertEqual(response.status_code, 200)
        self.assertTrue('page_obj' in response.context)
        
        response_2 = self.client.get(reverse('search')+'?page=2')
        self.assertEqual(response_2.status_code, 200)
        self.assertTrue('page_obj' in response.context)

    def test_search_by_actor(self):
        # Create 13 search for pagination
        list_movie_by_actor  = Actor.objects.search_movie_actor('bruce willis')
        response = self.client.post(reverse('search'),{'search': 'bruce willis'})
        self.list_movie_actor  = Movie.objects.filter(actor__in=list_movie_by_actor)  
        self.assertEqual(response.status_code, 200)
        self.assertTrue('page_obj' in response.context)
        
        response_2 = self.client.get(reverse('search')+'?page=2')
        self.assertEqual(response_2.status_code, 200)
        self.assertTrue('page_obj' in response.context)
        
        
