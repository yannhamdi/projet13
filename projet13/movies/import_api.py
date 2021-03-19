""" module that import products from imdb api"""

import requests

import os
api_key = os.environ.get("API_IMDB")


def get_json():
    """method that look for best rated movies api"""
    url = "https://imdb8.p.rapidapi.com/title/get-top-rated-movies"
    headers = {
               
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }
    url_2 =  "https://movie-database-imdb-alternative.p.rapidapi.com/"
    headers_2 = {
    'x-rapidapi-key': api_key,
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }

             
    response = requests.request("GET", url, headers=headers)
    movies = []
    if response.status_code == 200:
        movies = response.json()[0]['id'][7:16]
    for i in range(0,1):
        querystring = {"i":str(movies),"r":"json"}
        response_2 = requests.request("GET", url_2, headers=headers_2, params=querystring)
        movies_details = []
        movies_details = response_2.json()
        print(movies_details)

    

    
    


def main():
    get_json()

main()



