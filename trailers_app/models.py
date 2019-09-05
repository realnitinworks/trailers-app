import re

from django.db import models
from django.urls import reverse


class Movie(models.Model):
    title = models.CharField(max_length=300)
    plot = models.CharField(max_length=500)
    poster_url = models.URLField()
    trailer_url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('trailers_app:movie_detail', args=(self.id, ))

    def get_trailer_id(self):
        id_match = re.search(
            r'(?<=v=)[^&#]+', str(self.trailer_url))
        id_match = id_match or re.search(
            r'(?<=be/)[^&#]+', str(self.trailer_url))

        return (
            id_match.group(0)
            if id_match
            else None
        )