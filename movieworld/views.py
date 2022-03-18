from contextlib import nullcontext
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect,  JsonResponse
from django.urls import reverse
from django.template import loader
from movieworld.models import Movie, Review, UserProfile
import requests
from django.db.models import Avg
from django.utils.text import slugify
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from movieworld.forms import UserForm, UserProfileForm, RateForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
# from django.core.paginator import Paginator
# from django.shortcuts import render, get_object_or_404

# Create your views here.


#from movieworld.models import Review, UserProfile 


#@Author Xinyao 

def index(request):	
    
	top5movies_list = Review.objects.order_by('review_number')[:5]

	context_dict = {}
	context_dict['movies'] = top5movies_list
	
	response = render(request, 'movieworld/index.html', context=context_dict)
	return response

@login_required   
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


@login_required
def movieDetails(request, imdb_id):
    if Movie.objects.filter(movie_id=imdb_id).exists():
        movie_data = Movie.objects.get(movie_id=imdb_id)
        reviews = Review.objects.filter(movie=movie_data)
        database = True

        context = {
			'movie_data': movie_data,
			'reviews': reviews,
			'database': database,
		}
        
    else:
        url = 'http://www.omdbapi.com/?apikey=394a7f6d&i=' + imdb_id
        response = requests.get(url)
        movie_data = response.json()
        
        m, created = Movie.objects.get_or_create(
            movie_id=movie_data['imdbID'],
            title=movie_data['Title'],
            year=movie_data['Year'],
            genre=movie_data['Genre'],
            language=movie_data['Language'],
            poster_url=movie_data['Poster'],
            plot=movie_data['Plot'],
            )

        m.save()
        database = False

        context = {
            'movie_data': movie_data,
            'database': database,
        }

    template = loader.get_template('movieworld/reviews.html')

    return HttpResponse(template.render(context, request))

@login_required
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

@login_required
def review(request, imdb_id):
	movie = Movie.objects.get(movie_id=imdb_id)
	user = request.user

	if request.method == 'POST':
		form = RateForm(request.POST)
		if form.is_valid():
			rate = form.save(commit=False)
			rate.user = user
			rate.movie = movie
			rate.save()
			return HttpResponseRedirect(reverse('movieworld:details', args=[imdb_id]))
	else:
		form = RateForm()

	template = loader.get_template('movieworld/review.html')

	context = {
		'form': form, 
		'movie': movie,
	}

	return HttpResponse(template.render(context, request))

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

def user_login(request):
    return render(request, 'movieworld/login.html')

#@Author Tang 
@csrf_exempt
def login_check(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                 login(request, user)
                 request.session['user']=username
                 return JsonResponse({'res':1})
            else:
                 return JsonResponse({'res':2})
        else:
            return JsonResponse({'res':0})
    else:
        return render(request, 'movieworld/login.html')

#@Author Tang 
@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('movieworld:index'))

@csrf_exempt
def reviewed_select(request):

#get the username from the session
    user=request.session.get('user')
    
    try:
        language=request.POST.get('language')
        sort=request.POST.get('sort')
        genre=request.POST.get('genre')

    except:
        language=None
        sort=None
        genre=None

    try:
        user=User.objects.get(username=user)
        reviews=Review.objects.filter(user=user)

#set a flag to check if get data from review model or movie model
        flag=0

        if(language):
            movies=Movie.objects.filter(language__contains=language)
            flag=1

        if(genre):
            movies=Movie.objects.filter(genre__contains=genre)
            flag=1
        
        if sort=='a_z':
            movies=Movie.objects.order_by('title')
            flag=1
             
        if sort=='z_a' :
            movies=Movie.objects.order_by('-title')
            flag=1

        if sort=='asc':
                reviews=Review.objects.filter(user=user).order_by('date')

        if sort=="desc":
                reviews=Review.objects.filter(user=user).order_by('-date')

# make a list to save the data
        data=[]
        x=0    

#when select data from review model
        if (flag==0):
            for j in reviews:
                data.append([])
                data[x].append(j.movie.title)
                data[x].append(j.movie.year)
                data[x].append(j.movie.genre)
                data[x].append(j.movie.language)
                data[x].append(j.review)
                data[x].append(j.date.strftime('%Y-%m-%d %H:%I:%S'))
                data[x].append(j.review_number)
                x+=1

#when select data from movie model     
        if (flag==1):
            for i in movies: 
                reviews=Review.objects.filter(movie=i,user=user)            
                for j in reviews:
                    data.append([])
                    data[x].append(j.movie.title)
                    data[x].append(j.movie.year)
                    data[x].append(j.movie.genre)
                    data[x].append(j.movie.language)
                    data[x].append(j.review)
                    data[x].append(j.date.strftime('%Y-%m-%d %H:%I:%S'))
                    data[x].append(j.review_number)
                    x+=1
       
    except Movie.DoesNotExist:
        data=None

    return JsonResponse(data, safe=False)

@login_required
def my_reviews(request):

#get username from session
    user=request.session.get('user')
    user=User.objects.get(username=user)

#get all reviews from this user
    reviews = Review.objects.filter(user=user)
    context_dict = {}
    context_dict['reviews'] = reviews

    return render(request, 'movieworld/my_reviews.html', context=context_dict)

@login_required
@csrf_exempt
def movies_select(request):

#clear the session
    request.session['language']=None
    request.session['genre']=None

#get the two variables from dropdown
    try:
        language=request.POST.get('language')
        genre=request.POST.get('genre')

    except:
        language=None
        genre=None

#save the two options into session
    request.session['language']=language
    request.session['genre']=genre
    
    return JsonResponse({'res':1})

@login_required
def reviews_all(request):   

#get the option from session
    try:
        language=request.session.get('language')
        genre=request.session.get('genre')
        print(language)
    except:
        language=None
        genre=None

#get all movies 
    movies = Movie.objects.all()

#filter the movies if the option exists
    if language:
        movies=Movie.objects.filter(language__contains=language)
        request.session['language']=None

    if genre:
        movies=Movie.objects.filter(genre__contains=genre)
        request.session['genre']=None

#get the movie from review model with no duplicate values
    reviews=Review.objects.values('movie').distinct()

#return the movies and reviews
    context_dict={}
    context_dict['movies']=movies
    context_dict['reviews']=reviews

#make a flag to check if there is data meets the requirements 
    context_dict['flag']=0

#set the flag 1, when there is data    
    for m in movies:
        for r in reviews:
            if m.id==r['movie']:
                 context_dict['flag']=1               

    return render(request, 'movieworld/reviews_all.html', context=context_dict)
