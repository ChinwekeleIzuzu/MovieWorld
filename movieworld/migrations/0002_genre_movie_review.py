# Generated by Django 2.1.5 on 2022-02-28 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieworld', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('year', models.IntegerField(blank=True)),
                ('language', models.CharField(blank=True, max_length=250)),
                ('poster', models.URLField(blank=True)),
                ('genre', models.ManyToManyField(blank=True, to='movieworld.Genre')),
            ],
            options={
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_id', models.IntegerField(unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('review', models.TextField(blank=True, max_length=3000)),
                ('review_number', models.SmallIntegerField(choices=[(1, '1 - Do not Recomment'), (2, '2 - Bad'), (3, '3 - Reccomendable'), (4, '4 - Very Good'), (5, '5 - Master Piece')])),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieworld.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieworld.UserProfile')),
            ],
        ),
    ]
