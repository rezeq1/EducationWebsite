from django.db import models
from users.models import Kindergarten
# Create your models here.
class Quiz(models.Model):
    class Meta:
        verbose_name_plural = "Quiz"
        
class lesson(models.Model):
    garten=models.ForeignKey(Kindergarten, blank=True, null=True,on_delete=models.SET_NULL) 
    video_file = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=100)
    desc = models.TextField()
    quiz=models.OneToOneField(Quiz, on_delete=models.CASCADE)

 


    
    

