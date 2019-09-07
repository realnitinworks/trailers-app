from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from trailers_app.models import Movie


class MovieListView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movie_list.html'


class MovieDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movie_detail.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class MovieUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Movie
    fields = ('plot', 'poster_url', 'trailer_url')
    template_name = 'movie_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class MovieDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Movie
    template_name = 'movie_delete.html'
    success_url = reverse_lazy('trailers_app:movie_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ('title', 'plot', 'poster_url', 'trailer_url')
    template_name = 'movie_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


