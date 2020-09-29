from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer, URLSerializer, SearchMovieSerializer
from Movie_Serie.models import Movie_or_Serie, URL


class MovieGenericView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie_or_Serie.objects.all()
        imdb = self.request.query_params.get('imdb', None)
        status = self.request.query_params.get('status', None)
        genre = self.request.query_params.get('genre', None)
        available_4k = self.request.query_params.get('is_4k', None)
        available_fhd = self.request.query_params.get('is_fhd', None)
        available_hd = self.request.query_params.get('is_hd', None)

        statusParams = []
        genreParams = []

        if imdb is not None:
            queryset = queryset.filter(imdb__gte=imdb)
        if status is not None:
            for item in status.split(','):
                statusParams.append(item)
            queryset = queryset.filter(status__title__in=statusParams)
        if genre is not None:
            for item in genre.split(','):
                genreParams.append(item)
            queryset = queryset.filter(category__title__in=genreParams)
        if available_4k is not None:
            queryset = queryset.filter(available_4k__exact=available_4k)
        if available_fhd is not None:
            queryset = queryset.filter(available_fhd__exact=available_fhd)
        if available_hd is not None:
            queryset = queryset.filter(available_hd__exact=available_hd)
        return queryset


class URLGenericView(APIView):

    def get(self, request, slug, format=None):
        data = {}
        try:
            links = URL.objects.filter(movie_or_serie__slug__exact=slug)
        except URL.DoesNotExist:
            data['error'] = 'No data found.'
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer_class = URLSerializer(links, many=True)
        return Response(serializer_class.data)


class BestMovies(APIView):
    def get(self, request, format=None):
        data = {}
        try:
            movies = Movie_or_Serie.objects.filter(status__title__exact='movie').order_by('-imdb')
        except URL.DoesNotExist:
            data['error'] = 'No data found.'
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer_class = MovieSerializer(movies, many=True)
        return Response(serializer_class.data)


class BestSeries(APIView):
    def get(self, request, format=None):
        data = {}
        try:
            movies = Movie_or_Serie.objects.filter(status__title__exact='serie').order_by('-imdb')
        except Movie_or_Serie.DoesNotExist:
            data['error'] = 'No data found.'
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer_class = MovieSerializer(movies, many=True)
        return Response(serializer_class.data)


class ModelDetailView(APIView):
    def get(self, request, slug, format=None):
        data = {}
        try:
            movies = Movie_or_Serie.objects.get(slug__exact=slug)
        except Movie_or_Serie.DoesNotExist:
            data['error'] = 'No data found.'
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer_class = MovieSerializer(movies)
        return Response(serializer_class.data)


class LatestMoviesView(APIView):
    def get(self, request, format=None):
        data = {}
        try:
            movies = Movie_or_Serie.objects.filter(status__title__exact='movie').order_by('-added_date')[:5]
        except Movie_or_Serie.DoesNotExist:
            data['error'] = 'No data found.'
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer_class = MovieSerializer(movies, many=True)
        return Response(serializer_class.data)


class LatestSeriesView(APIView):
    def get(self, request, format=None):
        data = {}
        try:
            movies = Movie_or_Serie.objects.filter(status__title__exact='serie').order_by('-added_date')[:5]
        except Movie_or_Serie.DoesNotExist:
            data['error'] = 'No data found.'
            return Response(data=data, status=status.HTTP_404_NOT_FOUND)

        serializer_class = MovieSerializer(movies, many=True)
        return Response(serializer_class.data)

class AllMoviesAndSeriesView(generics.ListAPIView):
    pagination_class = None
    serializer_class = SearchMovieSerializer
    def get_queryset(self):
        movies = Movie_or_Serie.objects.all()
        return movies
