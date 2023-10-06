from django.db import models
# pylint: disable=invalid-str-returned
# pylint:disable=no-member


class Celebrity(models.Model):
    celebrity_id = models.AutoField(primary_key=True)
    celebrity_name = models.CharField(max_length=100)
    celebrity_image_url = models.URLField()

    def __str__(self):
        return self.celebrity_name


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100)

    def __str__(self):
        return self.movie_name


class MovieAndCelebritiesMapping(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    celebrity = models.ForeignKey(Celebrity, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.movie_name} - {self.celebrity.celebrity_name}"
