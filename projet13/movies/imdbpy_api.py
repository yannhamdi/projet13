"""module that extract imdi id"""
import imdb

def imdbpy_api(movie_title):
    """module that uses imdppy to extract id movie"""

    ia = imdb.IMDb()
    try:
        search = ia.search_movie(movie_title)
        print(search)
    except Exception as e:
        print("error: %s" % e)
def main():
    movie_title = "scarface"
    imdbpy_api(movie_title)
main()