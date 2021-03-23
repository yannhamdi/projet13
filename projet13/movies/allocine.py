import imdb
import os
import requests
api_key = os.environ.get("API_IMDB")
  

ia = imdb.IMDb()
search= ia.get_movie("8503618")
print(search.infoset2keys)
print(search['genres'])


    