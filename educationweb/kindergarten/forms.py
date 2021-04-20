from django import forms 
from .models import lesson
class LessonForm(forms.ModelForm):
    video_file = forms.FileField(required=False)
    desc = forms.CharField (widget=forms.Textarea,required=False) 
    class Meta:
        model=lesson
        fields=['title','video_file','desc']
        