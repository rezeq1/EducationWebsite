from django import forms 
from .models import lesson,Qustion
class LessonForm(forms.ModelForm):
    video_file = forms.FileField(required=False)
    desc = forms.CharField (widget=forms.Textarea,required=False) 
    video_file.widget.attrs.update({'accept':'video/*'})
    class Meta:
        model=lesson
        fields=['title','video_file','desc']

class QustionForm(forms.ModelForm):
    CHOICES = (('1', ' 1'),(' 2', ' 2'),(' 3', ' 3'),(' 4', ' 4'))
    rightAnswer = forms.ChoiceField(choices=CHOICES)
    class Meta:
        model=Qustion
        fields=['qustion','answer1','answer2','answer3','answer4','rightAnswer']
        