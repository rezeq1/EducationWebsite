from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from .models import * 
from django.core.exceptions import ValidationError 




def validate_email(value):
    if User.objects.filter(email = value).exists():
        raise ValidationError((f"{value} is taken."),params = {'value':value})

class ParentRegisterForm(UserCreationForm): 
    first_name = forms.CharField(max_length=30, required=True) 
    last_name = forms.CharField(max_length=30, required=True) 
    email = forms.EmailField(max_length=254,required=True,validators = [validate_email] ) 
    username = forms.CharField(max_length=30, required=True)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput() 
    class Meta: 
        model = Parent 
        
        fields = [ 'username',
         'first_name',
          'last_name', 'email', 
          'password1', 'password2', ] 


class TeacherRegisterForm(UserCreationForm): 
    first_name = forms.CharField(max_length=30, required=True) 
    last_name = forms.CharField(max_length=30, required=True) 
    email = forms.EmailField(max_length=254,required=True,validators = [validate_email] ) 
    username = forms.CharField(max_length=30, required=True)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput() 
    class Meta: 
        model = Teacher 
        fields = [ 'username',
         'first_name',
          'last_name',
           'email', 
          'password1',
           'password2', ] 


class KidRegisterForm(UserCreationForm): 
    first_name = forms.CharField(max_length=30, required=True) 
    last_name = forms.CharField(max_length=30, required=True) 
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254,required=True,validators = [validate_email] ) 
    age = forms.IntegerField(required=True)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput() 
    class Meta: 
        model = Kid 
        fields = [ 'username',
         'first_name',
          'last_name',
          'age',
           'email', 
          'password1',
           'password2', ] 


class AddToKindergartenForm(forms.ModelForm):
    kindergarten = forms.ModelChoiceField(queryset=Kindergarten.objects.all())
    class Meta:      
        model = Kindergarten
        fields = ['kindergarten']

class KindergartenRegisterForm(forms.ModelForm): 
    name = forms.CharField(max_length=30, required=True) 
    seatLimit = forms.IntegerField(required=True)

    class Meta: 
        model = Kindergarten 
        fields = [ 'name','seatLimit',]


class ChangePasswordForm(UserCreationForm):

    password = forms.PasswordInput()   
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput() 

    class Meta: 
        model = User 
        fields = ['password', 'password1','password2',]


class RequestPasswordForm(forms.Form):
    email = forms.EmailField(max_length=254,required=True ) 
    username = forms.CharField(max_length=30, required=True)
    class Meta: 
        model = User 
        fields = [ 'username', 'email',  ]