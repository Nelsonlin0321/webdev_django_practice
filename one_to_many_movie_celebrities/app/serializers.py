# serializers.py
from rest_framework import serializers
from .models import Celebrity, Movie, MovieAndCelebritiesMapping


class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = ['celebrity_id', 'celebrity_name', 'celebrity_image_url']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_id', 'movie_name']


class MovieCelebritiesMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieAndCelebritiesMapping
        fields = ['movie_id', 'celebrity_id']
