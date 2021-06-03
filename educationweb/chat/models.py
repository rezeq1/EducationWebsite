from users.models import *


from django.db import models
from django.contrib.auth.models import User
# Create your models here.






class Chat(models.Model):
    participants = models.ManyToManyField(
        User, related_name='chats', blank=True)
    
    garten=models.ForeignKey(Kindergarten,blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}".format(self.pk)
class Message(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    sender = models.ForeignKey(User,related_name='messages',on_delete=models.CASCADE)
    sender_type = models.CharField(verbose_name="Chat room type", max_length=30)
    chat=models.ForeignKey(Chat,related_name='messages',on_delete=models.CASCADE)
    read=models.BooleanField(default=True)

