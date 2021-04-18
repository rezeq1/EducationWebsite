from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Parent(User):

    class Meta:
        verbose_name_plural = "Parent" 
   
    def __str__(this):
        return this.username



class Teacher(User):

    class Meta:
        verbose_name_plural = "Teacher" 
    def __str__(this):
        return this.username


class Kindergarten(models.Model):
    seatLimit=models.IntegerField()
    name=models.CharField(max_length=100,primary_key=True)
    myTeacher = models.OneToOneField(Teacher,  on_delete=models.CASCADE, primary_key=False)
    def __str__(this):
        return this.name

class Kid(User):
    age=models.IntegerField()
    myParent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    garten=models.ForeignKey(Kindergarten, blank=True, null=True,on_delete=models.SET_NULL) 
    class Meta:
        verbose_name_plural = "Kid"
        

