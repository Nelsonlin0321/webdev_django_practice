from django.urls import path, include
from rest_framework import routers
from . import views

# pylint:disable=no-member
urlpatterns = [
    path('celebrities/',
         views.get_celebrities_for_movie, name="get_celebrities_for_movie"),
    path('movies/celebrities',
         view=views.MovieCelebritiesViewSet.as_view({'get': 'list'}),
         name="celebrities_for_movie"),
]
