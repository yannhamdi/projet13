from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from movies.models import Movie
from favorites.models import Favorite
from movies.forms import ProductSearch

@login_required
def saving_search(request, id_movie):
    """views to save the user's search"""
    movie = Movie.objects.get(id_code=id_movie)
    Favorite.objects.get_or_create(user_link=request.user,
                                   movie_saved=movie)
    return redirect('home')


@login_required
def display_account(request):
    """views that display searched details"""
    form = ProductSearch(request.POST or None)
    favoris = Favorite.objects.filter(
        user_link=request.user).order_by('movie_saved')
    paginator = Paginator(favoris, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'display_account.html', {'page_obj': page_obj, 'form': form})