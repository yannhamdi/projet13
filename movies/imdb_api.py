"""module that import top rated films from imdb api"""
import os

import requests

api_movie_db = os.environ.get("API_MOVIE_DB")


def imdb_api():
    """method that look for best rated movies api"""
    movies_title = []
    for num_page in range(1, 2):
        response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=" +
                                api_movie_db + "&language=en-US&page=" + str(num_page))
        movies = []
        movies = response.json()['results']
        for element in movies:
            movies_title.append(element["title"])
    movies_title = set(movies_title)
    movies_title = list(movies_title)
    return movies_title
