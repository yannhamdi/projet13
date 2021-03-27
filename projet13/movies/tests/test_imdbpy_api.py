from django.test import TestCase
from unittest.mock import patch, Mock
from movies.imdbpy_api import imdbpy_api
import requests
import imdb


class TestImdbApi(TestCase):
    @patch('imdb.IMDb')
    def test_imdb_api(self,mock_imdbpy_api):
        movie_title= "die hard"
        mock_imdbpy_api = mock()

        mock_imdbpy_api.return_value =
                       { 23233232
              }


              
              
        
        mov =imdbpy_api(movie_title)
        self.assertEqual(mov, 23233232)
          
          