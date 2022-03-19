# Generated by Django 2.1.5 on 2022-03-19 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import movieworld.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.CharField(blank=True, max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('year', models.CharField(blank=True, max_length=25)),
                ('genre', models.CharField(blank=True, max_length=250)),
                ('language', models.CharField(blank=True, max_length=250)),
                ('poster', models.ImageField(blank=True, upload_to='movies')),
                ('poster_url', models.URLField(blank=True)),
                ('totalSeasons', models.CharField(blank=True, max_length=3)),
                ('plot', models.CharField(blank=True, max_length=900)),
            ],
            options={
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(blank=True, max_length=3000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('review_number', models.PositiveSmallIntegerField(choices=[(1, '1 - Do not Recommend'), (2, '2 - Bad'), (3, '3 - Reccomendable'), (4, '4 - Very Good'), (5, '5 - Master Piece')], default=0)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieworld.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=movieworld.models.user_directory_path)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
