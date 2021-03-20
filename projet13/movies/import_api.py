""" module that import products from imdb api"""

import requests

import os
api_key = os.environ.get("API_IMDB")
api_movie_db = os.environ.get("API_MOVIE_DB")


def get_json():
    """method that look for best rated movies api"""
    response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key="+ api_movie_db + "&language=en-US")
    movies = []
    movies = response.json()
    i = 0
    movies_title = []
    movies_release_date = []
    for i in range(len(movies["results"])):
        movies_title.append((movies["results"][i]["title"]))
        movies_release_date.append((movies["results"][i]["release_date"]))
    print(movies_title)
    print(movies_release_date)
    

    response = requests.request("GET", url, headers=headers, params=querystring)
    movies_details = []
    movies_details = response.json()
    url_2 = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    querystring_2 = {"s": "forrest gump","page":"1","r":"json"}

    headers_2 = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }
    response_2 = requests.request("GET", url, headers=headers_2, params=querystring_2)
    response_details = []
    if response_2.status_code == 200:
        response_details = response_2.json()["Search"][0]["imdbID"]
        print(response_details)
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

    querystring = {"i":"tt0109830","r":"json"}

    headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }
    
    
    

    
    


def main():
    get_json()

main()



