from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from movieworld.forms import UserForm, UserProfileForm
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