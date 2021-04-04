from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from .models import * 

class ParentRegisterForm(UserCreationForm): 
    first_name = forms.CharField(max_length=30, required=True) 
    last_name = forms.CharField(max_length=30, required=True) 
    email = forms.EmailField(max_length=254,required=True ) 
    username = forms.CharField(max_length=30, required=True)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput() 
    class Meta: 
        model = Parent 
        
        fields = [ 'username',
         'first_name',
          'last_name', 'email', 
          'password1', 'password2', ] 
