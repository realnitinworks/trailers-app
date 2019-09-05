from django.urls import path

from trailers_app.views import MovieListView, MovieDetailView, MovieUpdateView, MovieDeleteView, MovieCreateView

app_name = "trailers_app"

urlpatterns = [
    path("", MovieListView.as_view(), name="movie_list"),
    path("movie/<int:pk>/", MovieDetailView.as_view(), name="movie_detail"),
    path("movie/<int:pk>/edit/", MovieUpdateView.as_view(), name="movie_edit"),
    path("movie/<int:pk>/delete/", MovieDeleteView.as_view(), name="movie_delete"),
    path("movie/new/", MovieCreateView.as_view(), name="movie_new"),
]
