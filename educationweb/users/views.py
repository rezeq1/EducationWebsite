from django.shortcuts import render,redirect
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
            return redirect("login")
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
            return redirect("login")

    else:

        form=TeacherRegisterForm()
    return render(req,'users/register_teacher.html',{'form':form})


def home(req):
    return render(req,'users/home.html')

def kid_register(req):
    if req.method == 'POST':
        form=KidRegisterForm(req.POST)
        if form.is_valid():

            username=form.cleaned_data.get('username')
            parent=Parent.objects.filter(username=req.user.username).first()
            kid=form.save(commit=False)
            kid.myParent=parent
            kid.save()
            
            messages.success(req,f'Your son account has been created! you are now able to register him to a kindergarten ')
            return   render(req,'users/parent_home.html',{'user':req.user,'parent':True,'teacher':False,'kid':False})

    else:

        form=KidRegisterForm()
    return render(req,'users/register_kid.html',{'form':form})
