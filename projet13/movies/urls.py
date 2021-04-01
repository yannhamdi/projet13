from django.urls import path

from . import views

urlpatterns = [
    path('movie/<int:id>', views.lire, name='lire'),
    path('home', views.home, name='home'),
    path('search', views.search, name='search'),
    path('display_all', views.display_all, name='display_all'),

]