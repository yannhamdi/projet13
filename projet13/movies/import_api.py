""" module that import products from imdb api"""

import requests

import os

import random
import imdb

api_key = os.environ.get("API_IMDB")
api_movie_db = os.environ.get("API_MOVIE_DB")


def get_json():
    """method that look for best rated movies api"""

    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    headers = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }
    url_2 = "https://imdb8.p.rapidapi.com/title/find"
    headers_2 = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
    movies_title = []
    movies_id = []
    movies_details = []
    for num_page in range(1, 20):
        response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=" + api_movie_db + "&language=en-US&page=" + str(num_page))
        movies = []
        movies = response.json()
        for i in range(0, (len(movies["results"]))):
            movies_title.append(((movies["results"][(random.randint(0, len((movies["results"])))-1)]["title"])))
        movies_title_no = set(movies_title)
        movies_title_no = list(movies_title_no)
        print(len(movies_title_no))
        print(movies_title_no)
        for j in range(0, len(movies_title_no)):
            try:
                ia = imdb.IMDb()
                search = ia.search_movie(movies_title_no[j])
                movies_id.append(search[0].movieID)
            except:
                print(movies_title_no[j])
        h = 0
        movies_details = []
        for h in range(0, len(movies_id)):
            querystring_2 = {"i": "tt" + str(movies_id[h]),"r":"json"}
            response_3 = requests.request("GET", url, headers=headers, params=querystring_2) 
            try:
                movies_details.append(response_3.json())
            except:
                print(movies_id)
                continue
    print(len(movies_details))
       
def main():
    get_json()

main()



