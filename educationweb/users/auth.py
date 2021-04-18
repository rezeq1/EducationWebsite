from .models import *


class auth:
    def parent_register(self,parent):
        parent.save()
    def teacher_register(self,teacher):
        teacher.save()
    def kid_register(self,kid):
        kid.save()
    def delete_kid(req,kid):
        Kid.delete(kid)
    def delete_Parent(req,parent):
        Parent.delete(parent)
    def delete_Teacher(req,teacher):
        Teacher.delete(teacher)
    def kid_login(req,kid):
        return kid in Kid.objects.all()
    def change_password(self,oldpassword,newpassword,user):
        if user.check_password(oldpassword):
            user.set_password(newpassword)
            user.save()
            return True
        return False
    
