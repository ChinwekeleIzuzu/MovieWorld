from django import forms
from rango.models import UserProfile, Review
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password',)

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ( 'picture',)

class ReviewForm(forms.ModelForm):
	review=forms.CharField(max_length=200)

	class Meta:
		model = Review
		fields=('review',)
	