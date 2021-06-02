from django import forms 
from .models import *
from django.core.validators import MinValueValidator

class LessonForm(forms.ModelForm):
    video_file = forms.FileField(required=False)
    desc = forms.CharField (widget=forms.Textarea,required=False) 
    video_file.widget.attrs.update({'accept':'video/*'})
    class Meta:
        model=lesson
        fields=['title','video_file','desc']

class QuestionForm(forms.ModelForm):
    CHOICES = (('1', ' 1'),(' 2', ' 2'),(' 3', ' 3'),(' 4', ' 4'))
    answer = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model=Question
        fields=['question','option1','option2','option3','option4','answer']

class StoryForm(forms.ModelForm):
    class Meta:
        model=Story
        fields=['title']

class StoryPageForm(forms.ModelForm):
    
    class Meta:
        model=StoryPage
        fields=['page']

class HomeWorkForm(forms.ModelForm):
    subject=forms.CharField(max_length=50, required=True)
    duration=forms.IntegerField(required=True, validators=[MinValueValidator(1)])
    class Meta:
        model=HomeWork
        fields=['subject','duration']

class MusicForm(forms.ModelForm):
    music_file = forms.FileField(required=True)
    music_file.widget.attrs.update({'accept':'music/*'})
    class Meta:
        model=Music
        fields=['title','music_file']        