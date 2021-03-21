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

    response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key="+ api_movie_db + "&language=en-US&page=1")
    movies = []
    movies = response.json()
    i = 0
    movies_title = []
    for i in range(len(movies["results"])):
        movies_title.append((movies["results"][i]["title"]))
    response_details = []
    
    j = 0
    for j in range(len(movies_title)):
        querystring = {"q": movies_title[j]}
        response_2 = requests.request("GET", url_2, headers=headers_2, params=querystring)
        if response_2.status_code == 200:
            response_details.append(response_2.json()["d"][0]["id"])
    h = 0
    movies_details = []
    for h in range(len(response_details)):
        querystring_2 = {"i": response_details[h],"r":"json"}
        response_3 = requests.request("GET", url, headers=headers, params=querystring_2) 
        if response_3.status_code == 200:
            movies_details.append(response_3.json())
            
    
    


def main():
    get_json()

main()



