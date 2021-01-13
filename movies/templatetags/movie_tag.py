from django import template
from movies.models import Category, Movie

register = template.Library()


@register.simple_tag()
def get_categories():
    """Вивід всіх категорій"""
    return Category.objects.all()


@register.inclusion_tag("movies/tags/last_movies.html")
def get_last_movies(count):
    movies = Movie.objects.all().order_by('-id')[:count]
    return {'last_movies': movies}


@register.inclusion_tag("movies/tags/comment_list.html")
def get_comment_list(movie):
    reviews = movie.get_review()
    return {'reviews': reviews}


@register.inclusion_tag("movies/tags/inner_reviews.html")
def get_inner_reviews(review):
    inner_reviews = review.reviews_set.all()
    return {'inner_reviews': inner_reviews}
