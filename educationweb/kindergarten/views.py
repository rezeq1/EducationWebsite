from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from .forms import LessonForm,QustionForm,StoryForm,StoryPageForm
from .models import *
from .kindergarten_class import garten
from users.models import Teacher,Kindergarten
# Create your views here.


@login_required
def add_lesson(req):
    if req.method == 'POST':
        form=LessonForm(data=req.POST,files=req.FILES)
        if  'video_file' not  in  form.data or len(form.data['desc'])> 0:
            if form.is_valid() :
                l=form.save(commit=False)
                teacher=Teacher.objects.filter(username=req.user.username).first()
                KG=Kindergarten.objects.get(myTeacher=teacher)
                g=garten()
                quiz=g.add_lesson(l,KG)
                messages.success(req,f'The lesson has been uploaded')
                if 'has_quiz' in form.data:
                    return redirect("add_qustion",id=quiz.id)
                return redirect("KinderGartenHome")
        else:
            messages.warning(req,f'The lesson must have a video or description!!!')

    form=LessonForm()
    return render(req,'kindergarten/add_lesson.html',{'form':form})

@login_required
def add_story(req):
    if req.method == 'POST':
        form=StoryForm(data=req.POST,files=req.FILES)
    
        if form.is_valid() :
            s=form.save(commit=False)
            teacher=Teacher.objects.filter(username=req.user.username).first()
            KG=Kindergarten.objects.get(myTeacher=teacher)
            g=garten()
            g.add_Story(s,KG)
            return redirect("add_page",id=s.id)
    form=StoryForm()
    return render(req,'kindergarten/add_lesson.html',{'form':form})


@login_required
def add_Page(req,id=None):
    if req.method == 'POST':
        form=StoryPageForm(data=req.POST,files=req.FILES)
        if  'video_file' not  in  form.data or len(form.data['desc'])> 0:
            if form.is_valid() :
                q=form.save(commit=False)
                Page_id=form.data['Page_id']
                id=Page_id
                messages.success(req,f'The Page Has Been Uploaded')
                if 'has_next' not in form.data:
                    messages.success(req,f'The Story Has Been Uploaded')
                    return redirect("KinderGartenHome")
        else:
            messages.warning(req,f'The lesson must have a video or description!!!')

    form=StoryPageForm()
    story=Story.objects.filter(id=id).first()
    return render(req,'kindergarten/add_Page.html',{'form':form,'story':story,'id':id})

@login_required
def add_Qustion(req,id=None):
    if req.method == 'POST':
        form=QustionForm(data=req.POST,files=req.FILES)
        if  'video_file' not  in  form.data or len(form.data['desc'])> 0:
            if form.is_valid() :
                q=form.save(commit=False)
                quiz_id=form.data['quiz_id']
                id=quiz_id
                quiz=Quiz.objects.filter(id=quiz_id).first()
                g=garten()
                g.addQustion(q,quiz)
                messages.success(req,f'The qustion has been uploaded')
                if 'has_next' not in form.data:
                    return redirect("KinderGartenHome")
        else:
            messages.warning(req,f'The lesson must have a video or description!!!')

    form=QustionForm()
    return render(req,'kindergarten/add_qustion.html',{'form':form,'id':id})


@login_required
def lesson_info(req,id):
    l=lesson.objects.filter(id=id).first()
    quiz=l.quiz
    qustions=Qustion.objects.filter(quiz=quiz)
    return render(req,'kindergarten/lesson.html',{'lesson':l,'qustions':qustions})

@login_required
def KinderGartenHome(req):
    lessons=lesson.objects.all()
    return render(req,'kindergarten/KinderGartenHome.html',{'lessons':lessons})

