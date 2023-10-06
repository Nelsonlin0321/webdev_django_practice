from django.contrib import admin
from .models import Celebrity
from .models import Movie
from .models import MovieAndCelebritiesMapping

admin.site.register(Celebrity)
admin.site.register(Movie)
admin.site.register(MovieAndCelebritiesMapping)
