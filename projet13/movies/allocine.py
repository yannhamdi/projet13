import imdb
import os
import requests
api_key = os.environ.get("API_MOVIE_DB")
  
movie_genre = []
dicti = {}
ia = imdb.IMDb()
search= ia.get_movie("0087843")
print(search.infoset2keys)
print(search['cast'][1])
casting = str(search['cast'][1]) 
casting1 = str(search['cast'][0]) 
dicti['cast'] = casting
dicti['cast'] += ", " + casting1
print(dicti)
print(search['title'])
print(search['runtimes'])
print(search['year'])
print(search['cover url'])
print(search['genres'])
print(search['plot'][0])

response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=" + api_key + "&language=en-US")
movies = []
movies = response.json()
print(len(movies["results"]))