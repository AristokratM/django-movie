from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView, ListView
from .models import Movie
from .forms import ReviewForm
# Create your views here.


class MoviesView(ListView):
    """Список фільмів"""
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Детельна інформація про фільм"""
    queryset = Movie.objects.filter(draft=False)


class AddReview(View):
    """Додати відгук"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(pk=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolut_url())

