from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator

from movies.models import Movie

def index(request):
    list_movie = Movie.objects.all()
    paginator = Paginator(list_movie, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'movies/index.html', {'page_obj': page_obj})

def lire(request, id):
    movie = get_object_or_404(Movie.objects.filter(id_code=id))
    cast = movie.actor.all()
    return render(request, 'movies/lire.html',
                  {'movie': movie, 'cast': cast})