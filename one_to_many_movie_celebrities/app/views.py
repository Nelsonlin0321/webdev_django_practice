from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Celebrity, Movie, MovieAndCelebritiesMapping
# pylint:disable=no-member


@api_view(['GET'])
def get_celebrities_for_movie(request):
    movie_id = request.GET.get('movie_id')
    mappings = MovieAndCelebritiesMapping.objects.filter(movie_id=movie_id)
    celebrities = [mapping.celebrity for mapping in mappings]
    data = {
        'celebrities': [
            {
                'celebrity_id': celebrity.celebrity_id,
                'celebrity_name': celebrity.celebrity_name,
                'celebrity_image_url': celebrity.celebrity_image_url
            }
            for celebrity in celebrities
        ]
    }
    return Response(data)
