from pickle import TRUE
from django.db import models
<<<<<<< HEAD
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

=======
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to = 'profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Genre(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.title.replace(" ", "")
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Movie(models.Model):

    movie_id = models.CharField(max_length=20, primary_key=True, unique=True)
    title = models.CharField(max_length=200, unique=True)
    year = models.IntegerField(blank = True)
    genre = models.ManyToManyField(Genre, blank=True)
    language = models.CharField(max_length=250, blank=True)
    poster = models.URLField(blank = True)

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title

class Review(models.Model):
    review_id = models.IntegerField(unique=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    review= models.TextField(unique=False, null=False)
    review_number = models.SmallIntegerField(unique=False, null=False)

    def __str__(self):
        return self.review
>>>>>>> 495e348404d2a17fa43180f8c3b45657a81beba8
