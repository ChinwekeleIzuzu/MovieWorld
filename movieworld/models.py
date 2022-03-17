from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.core import files
import requests
from io import BytesIO
from PIL import Image

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to = 'profile_images', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 250, 250
        
        if self.picture:
            pic = Image.open(self.picture.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.picture.path)

    def __str__(self):
        return self.user.username


class Movie(models.Model):

    movie_id = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=25, blank = True)
    genre = models.CharField(max_length=250, blank=True)
    language = models.CharField(max_length=250, blank=True)
    poster = models.ImageField(upload_to='movies', blank = True)
    poster_url = models.URLField(blank=True)
    totalSeasons = models.CharField(max_length=3, blank=True)
    plot = models.CharField(max_length=900, blank=True)

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.poster == '' and self.poster_url !='':
            value = requests.get(self.poster_url)
            pb = BytesIO()
            pb.write(value.content)
            pb.flush()
            file_name = self.poster_url.split("/")[-1]
            self.poster.save(file_name, files.File(pb), save=False)
        return super().save(*args, **kwargs)
        
CHOICES = [
	(1, '1 - Do not Recommend'),
	(2, '2 - Bad'),
	(3, '3 - Reccomendable'),
	(4, '4 - Very Good'),
	(5, '5 - Master Piece'),
]

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField(max_length=3000, blank=True)
    review_number = models.PositiveSmallIntegerField(default=0, choices=CHOICES)

    def __str__(self):
        return self.user.username