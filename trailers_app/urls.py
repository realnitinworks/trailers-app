from django.urls import path

from trailers_app.views import MovieListView

app_name = "trailers_app"

urlpatterns = [
    path("", MovieListView.as_view(), name="movie_list")
]
