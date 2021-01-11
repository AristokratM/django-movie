from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import DetailView, ListView
from .models import Movie
# Create your views here.


class MoviesView(ListView):
    """Список фільмів"""
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Детельна інформація про фільм"""
    queryset = Movie.objects.filter(draft=False)

