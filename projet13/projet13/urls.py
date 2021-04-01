from django.urls import include, path

urlpatterns = [
    path('movies/', include('movies.urls')),
    path('users/', include('users.urls'))
   
]