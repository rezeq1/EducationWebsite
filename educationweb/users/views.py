from django.shortcuts import render,redirect
from .auth import auth
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .Kindergarten_methods import *
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
# Create your views here.


UserModel = get_user_model()

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
                model=Kindergarten_methods(kindergarten)
                model.add_kid(kid)
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

@login_required
def delete_teacher(req):
    username=req.user.username
    Teacher.delete(req.user)
    messages.success(req,f'{username} account has been deleted!')

    return redirect('login')

@login_required
def Kindergarten_register(req):
    if req.method == 'POST':
        form=KindergartenRegisterForm(req.POST)
        if form.is_valid():

            name=form.cleaned_data.get('name')
            seatLimit=form.cleaned_data.get('seatLimit')
            teacher=Teacher.objects.filter(username=req.user.username).first()
            Kindergarten_obj=Kindergarten(name=name,seatLimit=seatLimit,myTeacher=teacher)
            model=Kindergarten_methods(Kindergarten_obj)
            model.create(teacher)
            messages.success(req,f'Your kindergarten has been created!')
            return home(req)
    else:

        form=KindergartenRegisterForm()
    return render(req,'users/register_kindergarten.html',{'form':form})


@login_required
def ChangePassword(req):
    if req.method == 'POST':
        form=ChangePasswordForm(req.POST)
        if form.is_valid():
            user=req.user
            user2=form.save(commit=False)
            oldpassword=form.cleaned_data.get('password')
            password=form.cleaned_data.get('password1')
            model=auth()
            if  model.change_password(oldpassword,password,user):
                update_session_auth_hash(req, req.user)
                messages.success(req,f'Your password has been changed!')
                return home(req)
            messages.warning(req,f'Incorrect old password !')
    else: 
        form=ChangePasswordForm()
    return render(req,'users/ChangePassword.html',{'form':form})



def Reset_Password_confirm(req,username):
    if req.method == 'POST':
        form=ChangePasswordForm(req.POST)
        if form.is_valid():
            user=User.objects.filter(username=username).first()
            user2=form.save(commit=False)
            password=form.cleaned_data.get('password1')
            user.password=user2.password  
            user.save()



            messages.success(req,f'Your password has been changed!')
            return redirect('login')

    else: 
        form=ChangePasswordForm()
    return render(req,'users/ChangePassword.html',{'form':form})

def Reset_Password(req):
    if req.method == 'POST':
        form=RequestPasswordForm(req.POST)
        form.is_valid()
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        user=User.objects.filter(username=username,email=email).first()
        if user:
            return redirect("password_reset_confirm",username=username)
        messages.warning(req,f'Worng Details !')
        return render(req,'users/password_reset.html',{'form':form })

    else:

        form=RequestPasswordForm()
    return render(req,'users/password_reset.html',{'form':form })

def teacher_register(req):
    if req.method == 'POST':
        form=TeacherRegisterForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(req)
            mail_subject = 'Requeדsr for a new teacher account'
            message = render_to_string('users/account_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = "education.web.reset@gmail.com"
            email = EmailMessage(
                mail_subject, message, to=[to_email] 
            )
            email.send()
            messages.success(req,f'Your request has been sent to admin , check your email for admin response')
            return redirect('login')

    else:

        form=TeacherRegisterForm()
    return render(req,'users/register_teacher.html',{'form':form})

def activate(req, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        current_site = get_current_site(req)
        mail_subject = 'Registration completed'
        message = 'Admin activated your account'
        to_email = user.email
        email = EmailMessage(
             mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('Teacher account has been activated')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required
def show_rate(req,username):
    kid=Kid.objects.filter(username=username).first()
    rate = Rate.objects.filter(son=kid).first()
    return render(req,'users/show_rate.html',{'kid':kid,'rate':rate})

def rate_garten(request):

    if request.method == 'POST': 
        score = request.POST.get('score')
        sonName = request.POST.get('sonName')
        son = Kid.objects.filter(username=sonName).first()
        rate = Rate.objects.filter(son=son).first()
        if not rate :
            obj = Rate()
            obj.son = son
            obj.score = score
            obj.save()
        else:
            rate.score = score
            rate.save()

        return JsonResponse({'success':'true', 'score': score}, safe=False)
    return JsonResponse({'success':'false'})