from movieworld.models import UserProfile
from django import forms
from django.contrib.auth.models import User
from movieworld.models import Review, CHOICES

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

class RateForm(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)
	rate = forms.ChoiceField(choices=CHOICES, widget=forms.Select(), required=True)

	class Meta:
		model = Review
		fields = ('text', 'rate')