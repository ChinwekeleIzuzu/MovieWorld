import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_one.settings')

import django

django.setup()

from movieworld.models import Movie, Review, UserProfile, User

def populate():

    


    catch = [
        {'review':'Greatest Movie ever Made, might have plowed off in the middle',
        'date':'2022-03-15', 'review_number': 4},
        {'review':'Excitable Movie for sure, but terrible acting',
        'date':'2022-02-11', 'review_number': 2},
        ]

    pulp = [
        {'review':'Incredible',
        'date':'2022-03-15', 'review_number': 3},
        {'review':'Really Reccomend fam!',
        'date':'2022-03-15', 'review_number': 5},
        {'review':'Samuel L Jackson is da boss!',
        'date':'2022-03-15', 'review_number': 4} ]

    faceoff = [
        {'review':'Flat af!',
        'date':'2022-03-15', 'review_number': 1},
        ]

    batman = [
        {'review':'Best Batman ever',
        'date':'2022-03-15', 'review_number': 4},
        {'review':'Christopher Nolan is truly ahead of his time',
        'date':'2022-07-15', 'review_number': 3},
         ]

    harry = [
        {'review':'Harry Porter is the greatest Movie ever made!',
        'date':'2021-11-05', 'review_number': 5},
        {'review':'How do you not love Harry?',
        'date':'2022-03-15', 'review_number': 4} ]

    movies = {'tt0110912': {'reviews': pulp, 'title': 'Pulp Fiction', 'year': '1994', 'genre': 'Action, Triller, Suspense', 'language': 'English, Spanish, French', 'poster_url': 'https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg','plot': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'},
            'tt0119094': {'reviews': faceoff, 'title': 'Face/Off', 'year': '1994', 'genre': 'Action, Triller, Suspense', 'language': 'English, Spanish, French', 'poster_url': 'https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg', 'plot': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'},
            'tt0241527': { 'reviews': harry, 'title': 'Harry Potter and the Sorcerers Stone', 'year': '2001', 'genre': 'Adventure, Mystery, Suspence', 'language': 'English, Latin', 'poster_url': 'https://m.media-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_SX300.jpg', 'plot': 'An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world.'},
            'tt0264464':{
                'reviews': catch,
                'title': 'Catch Me if you Can',
                'year': '2002',
                'genre': 'Biopic, Triller, Suspence', 'language': 'English, French',
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMTY5MzYzNjc5NV5BMl5BanBnXkFtZTYwNTUyNTc2._V1_SX300.jpg',
                'plot': 'Barely 21 yet, Frank is a skilled forger who has passed as a doctor, lawyer and pilot. FBI agent Carl becomes obsessed with tracking down'
                    'the con man, who only revels in the pursuit.'},
            'tt0372784':{
                'reviews': batman,
                'title': 'Batman Begins',
                'year': '2005',
                'genre': 'Fiction, Adventure', 'language': 'English, Mandarin',
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BOTY4YjI2N2MtYmFlMC00ZjcyLTg3YjEtMDQyM2ZjYzQ5YWFkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg',
                'plot': 'After training with his mentor, Batman begins his fight to free crime-ridden Gotham City from corruption.'},

    }

    users = {'chinwekele':{
        'password': 123456},
    
    'yanlin':{
        'password': 123456},

    'xinyao':{
        'password': 123456},

    'yunpeng':{
        'password': 123456},
    }

    for use, u in users.items():
        c = add_user(use, u['password'])
       
    for mov, p in movies.items():
        m = add_movie(mov, p['title'], p['year'], p['genre'], p['language'], p['poster_url'],p['plot'])
        for r in p['reviews']:
            add_review(c, m, r['review'], r['date'], r['review_number'])
    

def add_user(user, password):
    u = User.objects.get_or_create(username=user)[0]
    u.password = password
    u.save()
    p = UserProfile.objects.get_or_create(user=u)[0]
    p.save()
    return p

def add_movie(movie_id, title, year, genre, language, poster_url, plot):
    m = Movie.objects.get_or_create(movie_id=movie_id)[0]
    m.title=title
    m.year=year
    m.genre=genre
    m.language=language
    m.poster_url=poster_url
    m.plot=plot
    m.save()
    return m

def add_review(use, mov, review, date, review_number):
    u = User.objects.get_or_create(username=use)[0]
    u.save()
    r = Review.objects.get_or_create(user=u, movie=mov, review=review)[0]
    r.date=date
    r.review_number=review_number
    r.save()
    return r


if __name__ == '__main__':
    print('Starting Movieworld population script')
    populate()