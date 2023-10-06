from django.urls import path
from . import views
# pylint:disable=no-member

urlpatterns = [
    path('celebrities/',
         views.get_celebrities_for_movie, name="get_celebrities_for_movie")
]
