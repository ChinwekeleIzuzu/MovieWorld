from django.db import models
form django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	user=models.OneToOneField(User, on_delelte=models.CASCADE)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __str__(self):
		return self.user.username


class Review(models.Model):
	MAX_LENGTH=200
	date=models.DateTimeField(auto_now_add=True)
	review=models.CharField(max_length=MAX_LENGTH)
	user=models.ManyToMany(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.id

