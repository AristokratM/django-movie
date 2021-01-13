from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic import DetailView, ListView
from .models import Movie, Actor, Genre
from .forms import ReviewForm
from .mixins import CategoriesMixin


# Create your views here.
class GenreYear():
    """Отримуємо всі жанри і роки"""

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values('year')


class MoviesView(GenreYear, ListView):
    """Список фільмів"""
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(GenreYear, DetailView):
    """Детельна інформація про фільм"""
    queryset = Movie.objects.filter(draft=False)


class AddReview(View):
    """Додати відгук"""

    def post(self, request, pk):
        print(request.POST)
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(pk=pk)
        print(movie)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
            print(form)
        return redirect(movie.get_absolut_url())


class ActorView(GenreYear, DetailView):
    """Детальна інформація про актора"""
    model = Actor
    template_name = "movies/actor.html"
    slug_field = "name"


class FilterMoviesView(GenreYear, ListView):

    def get_queryset(self):
        queryset = Movie.objects.filter(
            ( Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__name__in=self.request.GET.getlist("genre"))), draft=False
        )
        return queryset
