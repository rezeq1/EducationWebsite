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