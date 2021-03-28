from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('movie/<int:id>', views.lire, name='lire'),
]