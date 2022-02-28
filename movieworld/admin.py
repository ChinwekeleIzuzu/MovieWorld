from django.contrib import admin
<<<<<<< HEAD
from rango.models import UserProfile
from rango.models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
	list_display=('review','user','datetime')


admin.site.register(Review, ReviewAdmin)
=======
from movieworld.models import UserProfile, Movie, Review, Genre


# Register your models here.

# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('movie_id', 'title', 'year', 'genre', 'language')

# class ReviewAdmin(admin.ModelAdmin):
#     fields = ('review_id', 'username', 'movie_id', 'date', 'review', 'review_number')

# admin.site.register(Movie)
# admin.site.register(Review)
# admin.site.register(User) 
# admin.site.register(Genre)

>>>>>>> 495e348404d2a17fa43180f8c3b45657a81beba8
admin.site.register(UserProfile)
