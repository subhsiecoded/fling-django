from django import forms
from .models import Fling
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FlingForm(forms.ModelForm):
    class Meta:
        model = Fling
        fields = ['text', 'photo'] #make sure they match the variable name of the fields that u want to use from the model defined in models.py
#now we got to update the django views in the views.py file 

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
