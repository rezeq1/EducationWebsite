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
from kindergarten.models import *
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
        
        Garten=kid.garten
        if Garten:
            chat=Chat.objects.filter(garten=Garten).first() 
        else:
            chat = False
        print(chat) 
        board=Board.objects.filter(garten=kid.garten).first()
        messages=BoardMessage.objects.filter(board=board).all()
        return render(req,'users/kid_home.html',{'user':req.user,'parent':False,'teacher':False,'kid':True,'BoardMessages':messages,'chat':chat})
    
    teacher=Teacher.objects.filter(username=req.user.username).first()
    if teacher:
        try:
            Garten=Kindergarten.objects.get(myTeacher=teacher)
        except:
            HaveGarten = False
        else:
            HaveGarten = Garten.name
        
        messages = [ ]
        if HaveGarten :
            board=Board.objects.filter(garten=Garten).first()
            if req.method == 'POST' and req.POST.get('message'):
                msg=BoardMessage()
                msg.message=req.POST.get('message')
                msg.board=board
                msg.save()

            messages=BoardMessage.objects.filter(board=board).all()
            
        return render(req,'users/teacher_home.html',{'user':req.user,'parent':False,'teacher':True,'kid':False,'HaveGarten':HaveGarten,'BoardMessages':messages})


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

            board=Board()
            board.garten=Kindergarten_obj
            board.save()

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
            mail_subject = 'Request for a new teacher account'
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
    garten = kid.garten
    fullName = kid.first_name + " " +  kid.last_name

    numLesson = len(lesson.objects.filter(garten=garten).all())
    numViews = len(View.objects.filter(kid=kid).all())

    if numLesson !=0:
        AvGLesson = (numLesson/numViews)*100
    else:
        AvGLesson = 0

    numStory = len(Story.objects.filter(garten=garten).all())
    numStoryViews = len(ViewStory.objects.filter(kid=kid).all())

    if numStory !=0:
        AvGStory = (numStoryViews / numStory)*100
    else:
        AvGStory = 0

    numHW = len(HomeWork.objects.filter(garten=garten).all())
    numgrade = len(Grade.objects.filter(kid=kid).all())

    if numHW !=0:
        AvGHW = (numgrade / numHW)*100
    else:
        AvGHW = 0

    if numgrade != 0:
        AvgGrade = sum(list(map(lambda x: x.grade,Grade.objects.filter(kid=kid).all()))) / numgrade
    else:
        AvgGrade = 0

    rates = []

    for son in Kid.objects.filter(garten=garten).all():
        r = Rate.objects.filter(son=son).first()
        if r:
            rates.append(r)

    AvgRates = (sum(list(map(lambda x: x.score,rates))) / (len(rates)*5))*100

    res = {'kid':kid,'rate':rate,'numLesson':numLesson,'numViews':numViews,
    'numStory':numStory,'numStoryViews':numStoryViews,'numHW':numHW,'numgrade':numgrade,
    'AvgGrade':AvgGrade,'AvgRates':AvgRates,'fullName':fullName,'AvGLesson':AvGLesson,'AvGStory':AvGStory,'AvGHW':AvGHW}

    return render(req,'users/show_rate.html',res)

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


@login_required
def Change_Kindergarten(req,username):
    if req.method == 'POST':
        form=AddToKindergartenForm(req.POST)
        if form.is_valid():
            kindergarten=form.cleaned_data.get('kindergarten')
            Num_kids=len(kindergarten.kid_set.all())
            kid=Kid.objects.filter(username=username).first()

            if kid.garten == kindergarten:
                messages.warning(req,f'Your kid {username} stayed in her kindergarten !')
                return home(req)

            if Num_kids < kindergarten.seatLimit :
                model=Kindergarten_methods(kindergarten)
                model.Change_Kindergarten(kid)
                messages.success(req,f'Your kid {username} has been changed her kindergarten !')
                return home(req)
            else:
                form=AddToKindergartenForm()
                messages.warning(req,f'Kindergarten is full!')
                return render(req,'users/Kindergarten_Register.html',{'form':form ,'name':username})

    else:

        form=AddToKindergartenForm()
    return render(req,'users/Kindergarten_Register.html',{'form':form ,'name':username})


@login_required
def show_kindergarten_kids(req):
    garten=Kindergarten.objects.filter(myTeacher=req.user).first()
    kids=garten.kid_set.all()
    return render(req,'users/show_kindergarten_kids.html',{'kids':kids})

@login_required
def kick_kid(req,username):
    kid=Kid.objects.filter(username=username).first()
    model=Kindergarten_methods(None)
    model.Kick_From_Kindergarten(kid)
    messages.success(req,f'kid {username} has been kicked')
    return home(req)

@login_required
def Teatcher_Edit_info(req):
    if req.method == 'POST':
        teacher=Teacher.objects.filter(username=req.user.username).first()
        teacher.first_name = req.POST.get("firstname")
        teacher.last_name = req.POST.get("lastname")
        teacher.email = req.POST.get("email")
        if User.objects.filter(email = teacher.email).exists():
            messages.warning(req,f'email is already used !')
            return render(req,'users/Teatcher_Edit_info.html',{'teacher':teacher})

        teacher.save()
        messages.success(req,f'Changes saved')
        return home(req)
    else:
        teacher=Teacher.objects.filter(username=req.user.username).first()
    return render(req,'users/Teatcher_Edit_info.html',{'teacher':teacher})

@login_required
def Kid_Edit_info(req):
    if req.method == 'POST':
        kid=Kid.objects.filter(username=req.user.username).first()
        kid.first_name = req.POST.get("firstname")
        kid.last_name = req.POST.get("lastname")
        kid.email = req.POST.get("email")
        kid.age = int(req.POST.get("age"))
        if User.objects.filter(email = kid.email).exists():
            messages.warning(req,f'email is already used !')
            return render(req,'users/kid_Edit_info.html',{'kid':kid})

        kid.save()
        messages.success(req,f'Changes saved')
        return home(req)
    else:
        kid=Kid.objects.filter(username=req.user.username).first()
    return render(req,'users/kid_Edit_info.html',{'kid':kid})
    
    
