from django.views.generic import ListView

from trailers_app.models import Movie


class MovieListView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movie_list.html'

