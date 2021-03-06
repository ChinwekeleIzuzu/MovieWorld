from django.contrib import admin
from movieworld.models import UserProfile
from movieworld.models import Review
from movieworld.models import UserProfile, Movie, Review


class ReviewAdmin(admin.ModelAdmin):
	list_display=('review', 'user', 'date')


admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile)
admin.site.register(Movie)

