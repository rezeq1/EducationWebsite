from django import template
from .models import *

register = template.Library()


@register.simple_tag
def get_model1_object(user):
    parent=Parent.objects.filter(username=user.username).first()
    teacher=Teacher.objects.filter(username=user.username).first()
    kid=Kid.objects.filter(username=user.username).first()
    ans=[]
    if parent:
        ans.append(True)
    else:
        ans.append(False)
    
    HaveGarten = False
    if teacher:
        try:
            Garten=Kindergarten.objects.get(myTeacher=teacher)
        except:
            HaveGarten = False
        else:
            HaveGarten = Garten.name
        ans.append(True)
    else:
        ans.append(False)
    
    if kid:
        ans.append(True)
    else:
        ans.append(False)
    
    ans.append(HaveGarten)
    return ans