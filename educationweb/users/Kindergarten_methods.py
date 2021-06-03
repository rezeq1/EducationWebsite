from .models import *
from chat.models import Chat
class Kindergarten_methods():
    def __init__(self,kindergarten):
        self.kindergarten=kindergarten
    def create(self,teacher):
        self.kindergarten.myTeacher=teacher
        
        self.kindergarten.save()
        chat=Chat(garten=self.kindergarten)
        chat.save()
        chat.participants.add(teacher)

    def Change_Kindergarten(self,kid):
        kid.garten=self.kindergarten
        kid.save()

        
    def add_kid(self,kid):
        kid.garten=self.kindergarten
        chat=Chat.objects.filter(garten=self.kindergarten).first()
        chat.participants.add(kid)
        kid.save()

    def Kick_From_Kindergarten(self,kid):
        kid.garten.kid_set.remove(kid)

    def add_rate(self,score,kid):
        rate = Rate()
        rate.son = kid
        rate.score = score
        rate.save()
        return rate


    
