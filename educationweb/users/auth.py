from .models import *

class auth:
    def parent_register(self,parent):
        parent.save()
    def teacher_register(self,teacher):
        teacher.save()