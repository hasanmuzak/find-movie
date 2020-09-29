from rest_framework import serializers
from Movie_Serie.models import Movie_or_Serie, URL


class SearchMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_or_Serie
        fields = ['title', 'production_year', 'imdb', 'review_img', 'director', 'short_desc']


class MovieSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True, read_only=True)
    status = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Movie_or_Serie
        fields = (*[f.name for f in Movie_or_Serie._meta.fields], 'category', 'status')


class URLSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(source='movie_or_serie.slug', read_only=True)

    class Meta:
        model = URL
        fields = (*[f.name for f in URL._meta.fields], 'slug')
