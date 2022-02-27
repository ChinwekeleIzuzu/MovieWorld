from django.contrib import admin
from movieworld.models import User, Movie, Review, Genre


# Register your models here.

# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('movie_id', 'title', 'year', 'genre', 'language')

# class ReviewAdmin(admin.ModelAdmin):
#     fields = ('review_id', 'username', 'movie_id', 'date', 'review', 'review_number')

# admin.site.register(Movie)
# admin.site.register(Review)
# admin.site.register(User) 
# admin.site.register(Genre)