""" module that import products from imdb api"""

import requests

import os

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
    movies_details = {}
    movies_results = []
    for num_page in range(1,350):
        response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=" + api_movie_db + "&language=en-US&page=" + str(num_page))
        movies = []
        movies = response.json()
        for i in range(0, (len(movies["results"]))):
            movies_title.append(((movies["results"][i]["title"])))
        movies_title_no = set(movies_title)
        movies_title_no = list(movies_title_no)
        for j in range(0, len(movies_title_no)):
            try:
                ia = imdb.IMDb()
                search = ia.search_movie(movies_title_no[j])
                movies_id.append(search[0].movieID)
            except:
                print(movies_title_no[j])
        for h in range(0,len(movies_id)):
            search_details = ia.get_movie(movies_id[h])
            try:
                movies_details['id_code'] = movies_id[h]
                movies_details['movie_title'] = search_details['title']
                movies_details['run_time'] = search_details['runtimes']
                movies_details['movie_released'] = search_details['year']
                movies_details['image_movie'] = search_details['cover url']
                movies_details['plot'] = search_details['plot'][0]
                movies_details['genres'] = search_details['genres']
                movies_details['cast'] = str((search_details['cast'][0]))
                movies_details['cast'] +=  ", " + str((search_details['cast'][1]))

                movies_results.append(movies_details)
                movies_details = {}
                
            except Exception as e:
                print("notre resultat")
                print(len(movies_results))
                print(movies_id[h])
                print("error: %s" % e)
                continue
        print(len(movies_results))
        movies_id = []
        movies_title = []
        movies_title_no = []
    return movies_results
       



