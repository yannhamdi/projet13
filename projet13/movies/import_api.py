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
             
    response = requests.request("GET", url, headers=headers)
    movies = []
    if response.status_code == 200:
        movies = response.json()[0]['id']
        print(movies)
    print("erreur")
    


def main():
    get_json()

main()



