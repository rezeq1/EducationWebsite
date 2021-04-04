from django.shortcuts import render
from .auth import auth
from .forms import *
from django.contrib import messages
# Create your views here.

def parent_register(req):
    if req.method == 'POST':
        form=ParentRegisterForm(req.POST)
        if form.is_valid():
            au=auth()
            parent=form.save(commit=False)
            au.parent_register(parent)
            username=form.cleaned_data.get('username')
            messages.success(req,f'Your account has been created! you are now able to login ')
            return render(req,'users/home.html')
    else:

        form=ParentRegisterForm()
    return render(req,'users/register.html',{'form':form})



def teacher_register(req):
    if req.method == 'POST':
        form=TeacherRegisterForm(req.POST)
        if form.is_valid():
            au=auth()
            teacher=form.save(commit=False)
            au.teacher_register(teacher)
            username=form.cleaned_data.get('username')
            messages.success(req,f'Your account has been created! you are now able to login ')
            return render(req,'users/home.html')
    else:

        form=TeacherRegisterForm()
    return render(req,'users/register_teacher.html',{'form':form})


def home(req):
    return render(req,'users/home.html')
    