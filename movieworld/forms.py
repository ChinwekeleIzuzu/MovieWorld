from movieworld.models import UserProfile
from django import forms
from django.contrib.auth.models import User

#@Author Tang 
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)
        
#@Author Tang 
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)