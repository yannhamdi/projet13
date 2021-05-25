from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .forms import ProductSearch
from movies.models import Movie, Actor, Category

def display_all(request):
    """views that displays the whole database"""
    form = ProductSearch()
    all_movie = Movie.objects.all().order_by('id_code')
    paginator = Paginator(all_movie, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'movies/index.html', {'page_obj': page_obj, 'form':form})
    
def lire(request, id):
    movie = get_object_or_404(Movie.objects.filter(id_code=id))
    return render(request, 'movies/lire.html',
                  {'movie': movie})


def home(request):
    form = ProductSearch(request.POST or None)
    context = {'form': form}
    return render(request, 'movies/home.html', context)


def search(request):
    if not request.method == 'POST' and 'page' in request.GET:
        if 'search' in request.session:
            request.POST = request.session['search']
            request.method = 'POST'
        form = ProductSearch()
    if request.method == 'POST':
        form = ProductSearch(request.POST or None)
        request.session['search'] = request.POST
        if form.is_valid():
            prod = form.cleaned_data['search']
            list_movie_cat = Category.objects.search_movie_genre(prod)
            search_sub = Movie.objects.search_movie_title(prod)
            list_movie_by_actor = Actor.objects.search_movie_actor(prod)
            list_movie_cat = Category.objects.search_movie_genre(prod)
            if list_movie_by_actor:
                list_movie_actor = Movie.objects.filter(actor__in=list_movie_by_actor).order_by('actor')
                paginator_1 = Paginator(list_movie_actor, 10)
                page_number = request.GET.get('page')
                page_obj = paginator_1.get_page(page_number)
                return render(request, 'movies/index.html', {'page_obj': page_obj, 'form': form})
            if list_movie_cat:
                list_movie_by_cat = Movie.objects.filter(category__in=list_movie_cat).order_by('category')
                paginator = Paginator(list_movie_by_cat, 10)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request, 'movies/index.html', {'page_obj': page_obj, 'form': form})
            if search_sub:
                paginator = Paginator(search_sub, 10)
                page_number = request.GET.get('page')
                page_obj = paginator.get_page(page_number)
                return render(request, 'movies/index.html', {'page_obj': page_obj, 'form': form})
            return render(request, 'movies/no_response.html')

    else:
        form = ProductSearch()
        return render(request, 'movies/search.html', {'form': form})

def mention(request):
    form = ProductSearch(request.POST or None)
    context = {'form': form}
    return render(request, "movies/mentions_legales.html", context)
