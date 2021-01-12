from django.contrib import admin
from .models import Actor, Category, Genre, Movie, MovieShots, RatingStar, Rating, Reviews


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категорії"""
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)


class ReviewInline(admin.StackedInline):
    """Відгуки на сторінці фільму"""
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Фільми"""
    list_display = ('id', 'title', 'category', 'slug', 'draft')
    list_display_links = ('title',)
    list_filter = ('year', 'draft',)
    search_fields = ('title', 'category__name')
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    # fields = (('actors', 'directors', 'genres'), )
    fieldsets = (
        (None, {
            "fields": (('title', 'tagline'),)
        }),
        (None, {
            "fields": (('description', 'poster'),)
        }),
        (None, {
            "fields": (('year', 'world_premiere', 'country'),)
        }),
        ('Actor', {
            "classes": ('collapse',),
            "fields": (('actors', 'directors', 'genres', 'category'),)
        }),
        (None, {
            "fields": (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        ("Options", {
            "fields": (('slug', 'draft'),)
        }),
    )


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Відгуки"""
    list_display = ('id', 'name', 'text', 'movie', 'parent')
    readonly_fields = ('name', 'email')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанри"""
    list_display = ('id', 'slug', 'name')
    ordering = ('id',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Актори"""
    list_display = ('id', 'name', 'birth_date')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Кадри з фільму"""
    list_display = ('id', 'title', 'movie')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Рейтинг"""
    list_display = ('id', 'ip', 'star', 'movie')


admin.site.register(RatingStar)
