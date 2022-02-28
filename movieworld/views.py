from genericpath import exists
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from movieworld.models import Movie, Genre, Review, UserProfile
import requests
from django.utils.text import slugify
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from movieworld.forms import UserForm, UserProfileForm

# Create your views here.


#from movieworld.models import Review, UserProfile 

#@Author Xinyao 

def index(request):	
    # Need to build models and forms for Review
	# top5movies_list = Review.objects.order_by('-rating')[:5]

	context_dict = {}
	# context_dict['top5movies'] = top5movies_list
	
	response = render(request, 'movieworld/index.html', context=context_dict)
	return response
    
def search(request):
    
    query = request.GET.get('title')
    if query:
        url = 'http://www.omdbapi.com/?apikey=394a7f6d&s=' + query
        response = requests.get(url)
        movie_data = response.json()
        
        context_dict = {
                'query': query,
                'movie_data': movie_data,
                'page_no': 1,
                }

        template = loader.get_template('movieworld/result.html')
        return HttpResponse(template.render(context_dict, request))

    return render(request, 'movieworld/search.html')

def movieDetails(request, imdb_id):
    if Movie.objects.filter(movie_id=imdb_id).exists():
        movie_data = Movie.objects.get(movie_id=imdb_id)
        database = True
    else:
        url = 'http://www.omdbapi.com/?apikey=394a7f6d&i=' + imdb_id
        response = requests.get(url)
        movie_data = response.json()

        genre_objs = []

        genre_list = list(movie_data['Genre'].replace(" ", "").split(','))

        for genre in genre_list:
            genre_slug = slugify(genre)
            g, created = Genre.objects.get_or_create(title=genre, slug=genre_slug)
            genre_objs.append(g)

            m, created = Movie.objects.get_or_create(
                movie_id=movie_data['imdbID'],
                title=movie_data['Title'],
                year=movie_data['Year'],
                genre=movie_data[''],
                language=movie_data['Language'],
                poster_url=movie_data['poster'],
                )

            m.Genre.set(genre_objs)
        m.save()
        database = False

        context = {
            'movie_data': movie_data,
            'database': database,
        }

        template = loader.get_template('result.html') # stILL TO WORK ON THIS.

        return HttpResponse(template.render(context, request))

def page(request, query, page_no):
    url = 'http://www.omdbapi.com/?apikey=394a7f6d&s=' + query + '&page=' + str(page_no)
    response = requests.get(url)
    movie_data = response.json()

    page_no = int(page_no)+1

    context_dict = {
            'query': query,
            'movie_data': movie_data,
            'page_no': page_no,
            }

    template = loader.get_template('movieworld/result.html')
    return HttpResponse(template.render(context_dict, request))

#@Author Xinyao 
def about(request):
	context_dict = {}
	return render(request, 'movieworld/about.html', context_dict)

#@Author Tang 
def sign_up(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture'] 

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'movieworld/sign_up.html', context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

#@Author Tang 
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('movieworld:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'movieworld/login.html')

#@Author Tang 
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('movieworld:index'))
