from django.urls import include, path
from django.contrib import admin
from projet13.movies.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('users/', include('users.urls')),
    path('favorites/', include('favorites.urls')),
     path('', home, name="home"),
   
]