from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Password field.
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

    movie_id = models.CharField(primary_key=True, unique=True)
    title = models.CharField(max_length=200, unique=True)
    year = models.IntegerField(max_length=10, blank = True)
    genre = models.ManyToManyField(Genre, blank=True)
    language = models.CharField(max_length=250, blank=True)
    poster = models.URLField(blank = True)

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title

class Review:
    review_id = models.IntegerField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    review= models.TextField(unique=False, null=False)
    review_number = models.SmallIntegerField(unique=False, null=False)

    def __str__(self):
        return self.review_id