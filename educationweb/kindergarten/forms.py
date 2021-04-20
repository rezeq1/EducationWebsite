from django import forms 
from .models import lesson
class LessonForm(forms.ModelForm):
    class Meta:
        model=lesson
