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

<<<<<<< HEAD
=======


>>>>>>> 937088d18948e906995ab3bf33b78af196b8d814
def teacher_register(req):
    if req.method == 'POST':
        form=TeacherRegisterForm(req.POST)
        if form.is_valid():
            au=auth()
            teacher=form.save(commit=False)
            au.teacher_register(teacher)
            username=form.cleaned_data.get('username')
            messages.success(req,f'Your account has been created! you are now able to login ')
<<<<<<< HEAD
            return redirect("login")
=======
            return render(req,'users/home.html')
>>>>>>> 937088d18948e906995ab3bf33b78af196b8d814
    else:

        form=TeacherRegisterForm()
    return render(req,'users/register_teacher.html',{'form':form})


def home(req):
<<<<<<< HEAD
    return render(req,'users/home.html')
=======
    return render(req,'users/home.html')
    
>>>>>>> 937088d18948e906995ab3bf33b78af196b8d814
