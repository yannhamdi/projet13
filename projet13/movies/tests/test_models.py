from django.test import TestCase
from movies.models import Category, Movie, Actor


class TestProductsModel(TestCase):
    def test_product(self):
        category = Category.objects.create(cat="drama")
        self.assertEqual(category.cat, "drama")
        actors = Actor.objects.create(act="bruce willis")
        self.assertEqual(actors.act, "bruce willis")
        movie = Movie.objects.create(id_code=2344393, movie_title="die hard",run_time="103",movie_released="2005"
                                            ,image_movie="www.didjdijddj.com",plot="film de guerre et tirs")
        categ = Category.objects.get(cat=category.cat)
        movie.category.add(categ)
        movie.save()
        acto = Actor.objects.get(act=actors.act)
        movie.actor.add(acto)
        self.assertEqual(movie.id_code, 2344393)
        self.assertEqual(movie.movie_title, "die hard")
        self.assertEqual(movie.run_time, "103")
        self.assertEqual(movie.movie_released, "2005")
        self.assertEqual(movie.image_movie, "www.didjdijddj.com")
        self.assertEqual(movie.plot, "film de guerre et tirs")
        cate = movie.category.all()
        cate2= str(cate[0])
        aac = movie.actor.all()
        aac2 = str(aac[0])
        self.assertEqual(cate2, "drama")
        self.assertEqual(aac2, "bruce willis")
        self.assertEqual(movie.movie_title, Movie.__str__(movie))
        self.assertEqual(category.cat, Category.__str__(category))
        self.assertEqual(actors.act, Actor.__str__(actors))