import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_one.settings')

import django

django.setup()

from movieworld.models import Movie, Review, UserProfile, User

def populate():

    # user_one = [
    #     {'username': 'chinwekele',
    #     'password': 123456,
    #     'picture': 'https://m.media-amazon.com/images/M/MV5BMTY5MzYzNjc5NV5BMl5BanBnXkFtZTYwNTUyNTc2._V1_SX300.jpg'},
    # ]
    
    # user_two = [
    #     {'username': 'yanlin',
    #     'password': 435555,
    #     'picture':''},
    # ]

    # user_three = [
    #     {'username': 'xinyao',
    #     'password': 5454323,
    #     'picture':''},
    # ]

    # user_four = [
    #     {'user': 'yunpeng',
    #     'password': 5454323,
    #     'picture':''}
    # ]


    # movie_1 = [
    #         {'movie_id':'tt0264464',
    #         'title': 'Catch Me if you Can',
    #         'year': '2002',
    #         'genre': 'Biopic, Triller, Suspence', 'language': 'English, French',
    #         'poster_url': 'https://m.media-amazon.com/images/M/MV5BMTY5MzYzNjc5NV5BMl5BanBnXkFtZTYwNTUyNTc2._V1_SX300.jpg',
    #         'plot': 'Barely 21 yet, Frank is a skilled forger who has passed as a doctor, lawyer and pilot. FBI agent Carl becomes obsessed with tracking down'
    #             'the con man, who only revels in the pursuit.'},
    # ]

    # movie_2 = [
    #         {'movie_id':'tt0372784',
    #         'title': 'Batman Begins',
    #         'year': '2005',
    #         'genre': 'Fiction, Adventure', 'language': 'English, Mandarin',
    #         'poster_url': 'https://m.media-amazon.com/images/M/MV5BOTY4YjI2N2MtYmFlMC00ZjcyLTg3YjEtMDQyM2ZjYzQ5YWFkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg',
    #         'plot': 'After training with his mentor, Batman begins his fight to free crime-ridden Gotham City from corruption.'},
    # ]

    # movie_3 = [
    #         {'movie_id': 'tt0241527',
    #         'title': 'Harry Potter and the Sorcerers Stone', 'year': '2001', 'genre': 'Adventure, Mystery, Suspence', 'language': 'English, Latin',
    #         'poster_url': 'https://m.media-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_SX300.jpg',
    #         'plot': 'An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world.'},
    # ]

    # movie_4 = [
    #         {'movie_id': 'tt0110912',
    #         'title': 'Pulp Fiction',
    #         'year': '1994',
    #         'genre': 'Action, Triller, Suspense', 'language': 'English, Spanish, French',
    #         'poster_url': 'https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg',
    #         'plot': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'},
    #     ]

    # movie_5 = [
    #         {'movie_id': 'tt0119094',
    #         'title': 'Face/Off',
    #         'year': '1997',
    #         'genre': 'Action, Triller, Suspense', 'language': 'English, Latin',
    #         'poster_url': ' https://m.media-amazon.com/images/M/MV5BYzFjNzIxMmEtMzY5NS00YTgzLTkwYWEtN2FjMmY0NmNkZWY3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg',
    #         'plot': 'To foil a terrorist plot, an FBI agent undergoes facial transplant surgery to assume the identity of the criminal mastermind who murdered his only son, but the criminal wakes up prematurely and seeks revenge.'},
    #         ]



    # reviews = {
    # 'Greatest Movie of all time':{'user':user_one, 'movie': movie_1, 'date': 'March 15, 2022, 3:29 p.m.', 'review_number': 5},
    # 'Greatest Movie of all time':{'user':user_two, 'movie': movie_2, 'date': 'March 15, 2022, 3:29 p.m.', 'review_number': 5},
    # 'Greatest Movie of all time':{'user':user_three, 'movie': movie_3, 'date': 'March 15, 2022, 3:29 p.m.', 'review_number': 5},
    # 'Greatest Movie of all time':{'user':user_four, 'movie': movie_4, 'date': 'March 15, 2022, 3:29 p.m.', 'review_number': 5},
    # 'Greatest Movie of all time':{'user':user_three, 'movie': movie_5, 'date': 'March 15, 2022, 3:29 p.m.', 'review_number': 5},
    #         }

    
    # for r in reviews.items():
    #     for u in r['user']:
    #         add_user(u['username'], u['password'], u['picture'])
    #     for p in r['movie']:
    #         add_movie(p['movie_id'], p['title'], p['year'], p['genre'], p['language'], p['poster_url'],p['plot'])
        # add_review(review, u, p, r['date'], r['review_number'])

    
    # # for u in User.objects.all():
    # for m in Movie.objects.all():
    #     for r in Review.objects.filter(user=User, movie=m):
    #         print(f'- {m}: {r}')

        movies = {'tt0264464':{
                'title': 'Catch Me if you Can',
                'year': '2002',
                'genre': 'Biopic, Triller, Suspence', 'language': 'English, French',
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BMTY5MzYzNjc5NV5BMl5BanBnXkFtZTYwNTUyNTc2._V1_SX300.jpg',
                'plot': 'Barely 21 yet, Frank is a skilled forger who has passed as a doctor, lawyer and pilot. FBI agent Carl becomes obsessed with tracking down'
                    'the con man, who only revels in the pursuit.'},

                'tt0241527':{
                'title': 'Harry Potter and the Sorcerers Stone', 'year': '2001', 'genre': 'Adventure, Mystery, Suspence', 'language': 'English, Latin',
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BNjQ3NWNlNmQtMTE5ZS00MDdmLTlkZjUtZTBlM2UxMGFiMTU3XkEyXkFqcGdeQXVyNjUwNzk3NDc@._V1_SX300.jpg',
                'plot': 'An orphaned boy enrolls in a school of wizardry, where he learns the truth about himself, his family and the terrible evil that haunts the magical world.'},

                'tt0119094':{
                'title': 'Face/Off',
                'year': '1997',
                'genre': 'Action, Triller, Suspense', 'language': 'English, Latin',
                'poster_url': ' https://m.media-amazon.com/images/M/MV5BYzFjNzIxMmEtMzY5NS00YTgzLTkwYWEtN2FjMmY0NmNkZWY3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg',
                'plot': 'To foil a terrorist plot, an FBI agent undergoes facial transplant surgery to assume the identity of the criminal mastermind who murdered his only son, but the criminal wakes up prematurely and seeks revenge.'},
            
                'tt0110912':{
                'title': 'Pulp Fiction',
                'year': '1994',
                'genre': 'Action, Triller, Suspense', 'language': 'English, Spanish, French',
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg',
                'plot': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'},
            
                'tt0372784':{
                'title': 'Batman Begins',
                'year': '2005',
                'genre': 'Fiction, Adventure', 'language': 'English, Mandarin',
                'poster_url': 'https://m.media-amazon.com/images/M/MV5BOTY4YjI2N2MtYmFlMC00ZjcyLTg3YjEtMDQyM2ZjYzQ5YWFkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg',
                'plot': 'After training with his mentor, Batman begins his fight to free crime-ridden Gotham City from corruption.'},

                }


        users ={
            'chinwekele':{
            'password': 123456,
            'picture': ''},

            'yanlin':{
            'password': 435555,
            'picture':''},

            'xinyao':{
            'password': 5454323,
            'picture':''},

            'yunpeng':{
            'password': 5454323,
            'picture':''}
        }

        reviews = {
    'Greatest Movie of all time':{'user':user, 'movie': movies, 'date': 'March 15, 2022, 3:29 p.m.', 'review_number': 5},
    'Greatest Movie of all time':{'user':user, 'movie': movies, 'date': 'March 15, 2022, 3:29 p.m.', 'review_number': 5},
    'Greatest Movie of all time':{'user':user, 'movie': movies, 'date': 'March 15, 2022, 3:29 p.m.', 'review_number': 5},
    'Greatest Movie of all time':{'user':user, 'movie': movies, 'date': 'March 15, 2022, 3:29 p.m.', 'review_number': 5},
    'Greatest Movie of all time':{'user':user, 'movie': movies, 'date': 'March 15, 2022, 3:29 p.m.', 'review_number': 5},
            }

        
        for user, u in users.items():
            add_user(user, u['password'], u['picture'])

        for movie, m in movies.items():
            add_movie(movie, m['title'], m['year'], m['genre'], m['language'], m['poster_url'], m['plot'])

     
        for review, r in reviews.items():
            add_review(review, u, m, r['date'], r['review_number'])  

def add_user(user, password, picture):
    u = User.objects.get_or_create(username=user)[0]
    u.password = password
    u.save()
    p = UserProfile.objects.get_or_create(user=u)[0]
    p.picture=picture
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

def add_review(review, user, movie, date, review_number=0):
    r = Review.objects.get_or_create(review=review, user=user, movie=movie)[0]
    r.date=date
    r.review_number=review_number
    r.save()
    return r


if __name__ == '__main__':
    print('Starting Movieworld population script')
    populate()