from django.urls import path, reverse
from . import views

urlpatterns = [
path('saving_search/<int:id_movie>', views.saving_search, name='saving_search'),
path('display_account', views.display_account, name='display_account')

]