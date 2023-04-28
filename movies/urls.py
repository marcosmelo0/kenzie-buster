from django.urls import path
from movies.views import MovieView, DetailMovieView, MovieOrderView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", DetailMovieView.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderView.as_view()),
]
