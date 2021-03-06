from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic import DetailView, ListView
from .models import Movie, Actor, Genre
from .forms import ReviewForm, RatingForm, Rating
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
    paginate_by = 2
    paginate_orphans = 1


class MovieDetailView(GenreYear, DetailView):
    """Детельна інформація про фільм"""
    queryset = Movie.objects.filter(draft=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        context['form'] = ReviewForm()
        return context


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
    """Фільтр фільмів"""
    paginate_by = 2
    paginate_orphans = 1

    def get_queryset(self):
        queryset = Movie.objects.filter(
            (Q(year__in=self.request.GET.getlist("year")) |
             Q(genres__in=self.request.GET.getlist("genre"))), draft=False
        ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['year'] = ''.join(f"year={x}&" for x in self.request.GET.getlist("year"))
        context['genre'] = ''.join(f"genre={x}&" for x in self.request.GET.getlist("genre"))
        return context


class JsonFilterMoviesView(ListView):
    """Фільтр фільмів JSON"""

    def get_queryset(self):
        queryset = Movie.objects.filter(
            (Q(year__in=self.request.GET.getlist('year')) |
             Q(genres__in=self.request.GET.getlist('genre'))), draft=False
        ).distinct().values("title", "tagline", "slug", "poster")
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({'movies': queryset}, safe=False)


class AddStarRating(View):
    """Додавання рейтингу фільму"""

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDER_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get('movie')),
                defaults={'star_id': int(request.POST.get('star'))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


class Search(GenreYear, ListView):
    paginate_by = 2

    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = f"q={self.request.GET.get('q')}&"
        return context
