from django.contrib import admin
from django.urls import path
from Movie_Serie.api.models import MovieGenericView, URLGenericView, BestMovies, BestSeries, ModelDetailView, LatestMoviesView, LatestSeriesView, AllMoviesAndSeriesView

urlpatterns = [
    path('all', MovieGenericView.as_view()),
    path('all-in-one', AllMoviesAndSeriesView.as_view()),
    path('detail/<slug:slug>', ModelDetailView.as_view()),
    path('best/movies', BestMovies.as_view()),
    path('best/movies/latest', LatestMoviesView.as_view()),
    path('best/series/latest', LatestSeriesView.as_view()),
    path('best/series', BestSeries.as_view()),
    path('links/<slug:slug>', URLGenericView.as_view()),
]