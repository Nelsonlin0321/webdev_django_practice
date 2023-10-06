from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import MovieCelebritiesMappingSerializer, CelebritySerializer
from .models import MovieAndCelebritiesMapping

# pylint:disable=no-member


@api_view(['GET'])
def get_celebrities_for_movie(request):
    movie_id = request.GET.get('movie_id')
    mappings = MovieAndCelebritiesMapping.objects.filter(movie_id=movie_id)

    celebrities = [CelebritySerializer(
        mapping.celebrity).data for mapping in mappings]

    return Response(celebrities)


class MovieCelebritiesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MovieAndCelebritiesMapping.objects.all()

    def list(self, request):
        movie_id = request.query_params.get('movie_id')
        print("movie_id:", movie_id)
        if movie_id:
            queryset = MovieAndCelebritiesMapping.objects.filter(
                movie_id=movie_id)

            celebrities = [mapping.celebrity for mapping in queryset]
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

        else:
            queryset = MovieAndCelebritiesMapping.objects.none()

        serializer = MovieCelebritiesMappingSerializer(queryset, many=True)
        return Response(serializer.data)
