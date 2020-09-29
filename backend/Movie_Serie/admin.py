from django.contrib import admin
from .models import Movie_or_Serie, URL, Statu, Category


# Register your models here.

class Movie_or_Serie_Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'director','available_4k', 'available_fhd', 'available_hd']
    list_display_links = ['id', 'title']


class URL_Admin(admin.ModelAdmin):
    list_display = ['id', 'movie_or_serie', 'season_number', 'episode_number']
    list_display_links = ['id', 'movie_or_serie']


admin.site.register(Movie_or_Serie, Movie_or_Serie_Admin)
admin.site.register(URL, URL_Admin)
admin.site.register(Statu)
admin.site.register(Category)
