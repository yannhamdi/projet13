from django.test import TestCase
from unittest.mock import patch, Mock
from movies.imdb_api import imdb_api
import requests
import imdb
import os

api_movie_db = os.environ.get("API_MOVIE_DB")

class TestImdbApi(TestCase):
    @patch('requests.get')
    def test_imdb_api(self,mock_get_json):
        mock_get_json.return_value.json.return_value ={
        "results": [
          { "title": "die hard"
              


              }]
              }
        
        mov =imdb_api()
        self.assertEqual(len(mov), 1)
          