from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import profile



class userRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model  = User
        fields = ['username' , 'email' ,'password1' , 'password2']



class userUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' , 'email']


class profileUpdateForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['image']

