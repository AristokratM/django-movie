from django.contrib import admin
from .models import Actor, Category, Genre, Movie, MovieShots, RatingStar, Rating, Reviews
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'id')


admin.site.register(Actor)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)

