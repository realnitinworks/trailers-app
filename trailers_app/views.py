from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from trailers_app.models import Movie


class MovieListView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movie_list.html'


class MovieDetailView(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movie_detail.html'


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ('plot', 'poster_url', 'trailer_url')
    template_name = 'movie_edit.html'


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movie_delete.html'
    success_url = reverse_lazy('trailers_app:movie_list')


class MovieCreateView(CreateView):
    model = Movie
    fields = ('title', 'plot', 'poster_url', 'trailer_url')
    template_name = 'movie_new.html'


