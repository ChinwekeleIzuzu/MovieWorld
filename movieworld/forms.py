<<<<<<< HEAD
from django.contrib.auth.models import User
from django import forms

=======
from movieworld.models import UserProfile
from django import forms
from django.contrib.auth.models import User

#@Author Tang 
>>>>>>> 1105d171ff48efc7321df5779515c7febf2fa465
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
<<<<<<< HEAD
        fields = ('username', 'password',)
=======
        fields = ('username', 'password',)
        
#@Author Tang 
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
>>>>>>> 1105d171ff48efc7321df5779515c7febf2fa465
