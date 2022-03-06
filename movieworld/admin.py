from django.contrib import admin
from movieworld.models import UserProfile
from movieworld.models import Review
from movieworld.models import UserProfile, Movies, Review, Genre
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
	list_display=('review','user','date', 'review_number')


admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile)
admin.site.register(Movies)
admin.site.register(Genre)
