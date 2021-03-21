""" module that import products from imdb api"""

import requests

import os
api_key = os.environ.get("API_IMDB")
api_movie_db = os.environ.get("API_MOVIE_DB")


def get_json():
    """method that look for best rated movies api"""
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }
    url_2 = "https://imdb8.p.rapidapi.com/auto-complete"
    headers_2 = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
    num_page = 1
    movies_title = []
    movies_id = []
    for num_page in range(1,6):
        response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=" + api_movie_db + "&language=en-US&page=" + str(num_page))
        movies = []
        movies = response.json()
        for i in range(len(movies["results"])):
            movies_title.append((movies["results"][i]["title"]))
    for j in range(0, len(movies_title)):
        querystring = {"q": movies_title[j]}
        response_2 = requests.request("GET", url_2, headers=headers_2, params=querystring)
        try:
            movies_id.append(response_2.json()["d"][0]["id"])
            print(len(movies_id))
        except:
            continue

    print(len(movies_id))
        

    
    


def main():
    get_json()

main()



