from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from movieworld.forms import ReviewForm, UserForm, UserProfileForm
#from movieworld.models import Review, UserProfile 

#@Author Xinyao 
def index(request):	
    # Need to build models and forms for Review
	# top5movies_list = Review.objects.order_by('-rating')[:5]

	context_dict = {}
	# context_dict['top5movies'] = top5movies_list
	
	response = render(request, 'movieworld/index.html', context=context_dict)
	return response

#@Author Xinyao 
def about(request):
	context_dict = {}
	return render(request, 'movieworld/about.html',context_dict)
