from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('users/', include('users.urls')),
    path('favorites/', include('favorites.urls')),
   
]