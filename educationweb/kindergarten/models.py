from django.db import models
from users.models import *
# Create your models here.

class lesson(models.Model):
    garten=models.ForeignKey(Kindergarten, blank=True, null=True,on_delete=models.SET_NULL) 
    video_file = models.FileField(upload_to='video/%y')
    title = models.CharField(max_length=100)
    desc = models.TextField()

class Story(models.Model):
    title=models.CharField(default='Story',max_length=50)
    garten=models.ForeignKey(Kindergarten, blank=True, null=True,on_delete=models.SET_NULL)

class StoryPage(models.Model):
    page=models.ImageField(upload_to='stories')
    story=models.ForeignKey(Story,related_name='pages', blank=True, null=True,on_delete=models.SET_NULL)

class HomeWork(models.Model):
    subject=models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()
    garten=models.ForeignKey(Kindergarten, blank=True, null=True,on_delete=models.CASCADE) 

    class Meta:
        verbose_name_plural = "HomeWork"

    def __str__(this):
        return this.subject


class Question(models.Model):
    question=models.CharField(max_length=400)
    option1=models.CharField(max_length=400)
    option2=models.CharField(max_length=400)
    option3=models.CharField(max_length=400)
    option4=models.CharField(max_length=400)
    answer=models.CharField(max_length=400)
    homeWork=models.ForeignKey(HomeWork, blank=True, null=True,on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name_plural = "Question" 

    def __str__(this):
        return this.question

class View(models.Model):
    Lesson=models.ForeignKey(lesson, blank=True, null=True,on_delete=models.SET_NULL)
    kid = models.ForeignKey(Kid, blank=True, null=True,on_delete=models.SET_NULL)




    
    

