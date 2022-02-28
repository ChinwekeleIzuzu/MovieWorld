from django.contrib import admin
from rango.models import UserProfile
from rango.models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
	list_display=('review','user','datetime')


admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile)
