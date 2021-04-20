from django.db import models
from users.models import Kindergarten
# Create your models here.
class Quiz(models.Model):
    class Meta:
        verbose_name_plural = "Quiz"

class Qustion(models.Model):
    qustion=models.CharField(max_length=400)
    answer1=models.CharField(max_length=400)
    answer2=models.CharField(max_length=400)
    answer3=models.CharField(max_length=400)
    answer4=models.CharField(max_length=400)
    rightAnswer=models.CharField(max_length=400)
    quiz=models.ForeignKey(Quiz, blank=True, null=True,on_delete=models.SET_NULL)
        
class lesson(models.Model):
    garten=models.ForeignKey(Kindergarten, blank=True, null=True,on_delete=models.SET_NULL) 
    video_file = models.FileField(upload_to='video/%y')
    title = models.CharField(max_length=100)
    desc = models.TextField()
    quiz=models.OneToOneField(Quiz, on_delete=models.CASCADE)

 


    
    

