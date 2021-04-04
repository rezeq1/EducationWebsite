from django.shortcuts import render
from .auth import auth
from .forms import *
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
            return render(req,'users/login.html')
    else:

        form=ParentRegisterForm()
    return render(req,'users/register.html',{'form':form})