import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_one.settings')

import django

django.setup()

from movieworld.models import Movie, Review, User

def populate():

    user_one = [
        {'username': 'chinwekele'},
        {'password': 123456},
    ]

    user_two = [
        {'username': 'yanlin'},
        {'password': 435555},
    ]

    user_three = [
        {'username': 'xinyao'},
        {'password': 5454323},
    ]


    # user_four = [
    #     {'user': 'yunpeng'},
    # ]

    # review_one = [
    #     {'user': user_one},
    #     {'movie': movie_one},
    #     {'date': 'March 7, 2022, 8:07 p.m.'},
    #     {'review': 'A master piece'},
    #     {'review_number': 4},
    # ]

    # review_two = [
    #     {'user': user_two},
    #     {'movie': movie_two},
    #     {'date': 'March 7, 2022, 8:07 p.m.'},
    #     {'review': 'A master piece'},
    #     {'review_number': 5},
    # ]

    # review_three = [
    #     {'user': user_three},
    #     {'movie': movie_three},
    #     {'date': 'March 7, 2022, 8:07 p.m.'},
    #     {'review': 'A master piece'},
    #     {'review_number': 2},
    # ]

    # review_four = [
    #     {'user': user_four},
    #     {'movie': movie_four},
    #     {'date': 'March 7, 2022, 8:07 p.m.'},
    #     {'review': 'A master piece'},
    #     {'review_number': 4},
    # ]

    # review_five = [
    #     {'user': user_two},
    #     {'movie': movie_five},
    #     {'date': 'March 7, 2022, 8:07 p.m.'},
    #     {'review': 'A master piece'},
    #     {'review_number': 3},
    # ]

    # reviews = {'master piece': {'user': user_one, 'movie': movie_five, 'date': 'March 17, 2022, 8:07 p.m.', 'review_number': 3},
    #         'Review Two': {'user': user_two, 'movie': movie_three, 'date': 'March 07, 2022, 8:07 p.m.', 'review_number': 4},
    #         'Review Three': {'user': user_three, 'movie': movie_two, 'date': 'March 17, 2022, 8:07 p.m.', 'review_number': 5} }



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

    for movie, p in movies.items():
        add_movie(movie, p['title'], p['year'] ,p['genre'], p['language'], p['poster_url'], p['plot'])
        

    # for review, review_data in reviews.items():
    #     # for u in review_data['user']:
    #     #     add_user(u['username'])
    #     for p in review_data['movie']:
    #         add_movie(p['movie_id'], p['title'], p['year'], p['genre'], p['language'], p['poster_url'], p['plot'])

    #     r = add_review(review, User, p, review_data['date'], review_data['review'], review_data['review_number'])
        
    # # for u in User.objects.all():
    # for m in Movie.objects.all():
    #     for r in Review.objects.filter(user=User, movie=m):
    #         print(f'- {m}: {r}')


# def add_user(user):
#     u = User.objects.get_or_create(username=user)
#     # u.password=password
#     return u

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
    r = Review.objects.get_or_create(review=review)[0]
    r.date=date
    r.user=user
    r.movie=movie
    r.review_number=review_number
    r.save()
    return r


if __name__ == '__main__':
    print('Starting Movieworld population script')
    populate()