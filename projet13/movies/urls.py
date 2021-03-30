from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('movie/<int:id>', views.lire, name='lire'),
    path('home', views.home, name='home'),
    path('search', views.search, name='search'),
 
]