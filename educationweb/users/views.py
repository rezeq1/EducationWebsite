from django.shortcuts import render,redirect
from .auth import auth
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


@login_required
def home(req):
    parent=Parent.objects.filter(username=req.user.username).first()
    
    if parent:
        return render(req,'users/parent_home.html',{'user':req.user,'parent':True,'teacher':False,'kid':False})
    
    kid=Kid.objects.filter(username=req.user.username).first()
    if kid:
        return render(req,'users/kid_home.html',{'user':req.user,'parent':False,'teacher':False,'kid':True})
    
    teacher=Teacher.objects.filter(username=req.user.username).first()
    if teacher:
        try:
            Garten=Kindergarten.objects.get(myTeacher=teacher)
        except:
            HaveGarten = False
        else:
            HaveGarten = Garten.name

        return render(req,'users/teacher_home.html',{'user':req.user,'parent':False,'teacher':True,'kid':False,'HaveGarten':HaveGarten})


@login_required
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

@login_required
def show_kids(req):
    parent=Parent.objects.filter(username=req.user.username).first()
    kids=parent.kid_set.all()
    context={
        'kids':kids,
        'parent':True,'teacher':False,'kid':False
    }
    return render(req,'users/showKids.html',context)

@login_required
def Register_To_Kindergarten(req,username):
    if req.method == 'POST':
        form=AddToKindergartenForm(req.POST)
        if form.is_valid():
            kindergarten=form.cleaned_data.get('kindergarten')
            Num_kids=len(kindergarten.kid_set.all())

            if Num_kids < kindergarten.seatLimit :
                kid=Kid.objects.filter(username=username).first()
                kid.garten=kindergarten
                kid.save()
                messages.success(req,f'Your kid {username} has been added to a kindergarten !')
                return home(req)
            else:
                form=AddToKindergartenForm()
                messages.warning(req,f'Kindergarten is full!')
                return render(req,'users/Kindergarten_Register.html',{'form':form ,'name':username})

    else:

        form=AddToKindergartenForm()
    return render(req,'users/Kindergarten_Register.html',{'form':form ,'name':username})


@login_required
def delete_kid(req,username):
    kid=User.objects.filter(username=username).first()
    User.delete(kid)
    messages.success(req,f'{username} account has been deleted!')

    return home(req)



@login_required
def delete_parent(req):
    username=req.user.username
    Parent.delete(req.user)
    messages.success(req,f'{username} account has been deleted!')

    return redirect('login')

    