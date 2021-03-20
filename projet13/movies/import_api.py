""" module that import products from imdb api"""

import requests

import os
api_key = os.environ.get("API_IMDB")
api_movie_db = os.environ.get("API_MOVIE_DB")


def get_json():
    """method that look for best rated movies api"""
    response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key="+ api_movie_db + "&language=en-US&page=1")



    movies = []
    movies = response.json()["results"][19]["release_date"]
    print(movies)
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

    querystring = {"i":"tt0109830","r":"json"}

    headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    movies_details = []
    movies_details = response.json()
    url_2 = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    querystring_2 = {"s":"Forrest Gump","page":"1","y":"1994-07-06","r":"json"}

    headers_2 = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }

    response_2 = requests.request("GET", url, headers=headers_2, params=querystring_2)
    response_details = []
    response_details = response_2.json()
    print(response_details)

    
    
    

    
    


def main():
    get_json()

main()



