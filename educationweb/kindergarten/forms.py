from django import forms 
from .models import *
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

        