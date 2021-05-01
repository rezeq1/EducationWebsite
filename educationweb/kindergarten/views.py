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
from .forms import *
from .models import *
from .kindergarten_class import garten
from users.models import *
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
                g.add_lesson(l,KG)
                messages.success(req,f'The lesson has been uploaded')
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
    return render(req,'kindergarten/add_story.html',{'form':form})

@login_required
def add_Page(req,id=None):
    if req.method == 'POST':
        form=StoryPageForm(data=req.POST,files=req.FILES)
        
        if form.is_valid() :
            SP=form.save(commit=False)
            Page_id=form.data['Page_id']
            id=Page_id
            s=Story.objects.filter(id=id).first()
            g=garten()
            g.add_Page(SP,s)
            messages.success(req,f'The Page Has Been Uploaded')
            if 'has_next' not in form.data:
                messages.success(req,f'The Story Has Been Uploaded')
                return redirect("KinderGartenHome")
        

    form=StoryPageForm()
    story=Story.objects.filter(id=id).first()
    return render(req,'kindergarten/add_Page.html',{'form':form,'story':story,'id':id})






@login_required
def lesson_info(req,id):
    l=lesson.objects.filter(id=id).first()
    return render(req,'kindergarten/lesson.html',{'lesson':l})

@login_required
def story_info(req,id):
    s=Story.objects.filter(id=id).first()
    pages=StoryPage.objects.filter(story=s)
    print(pages)
    return render(req,'kindergarten/story.html',{'story':s,'pages':pages})

@login_required
def KinderGartenHome(req):
    teacher=Teacher.objects.filter(username=req.user.username).first()
    KG=Kindergarten.objects.filter(myTeacher=teacher).first()
    lessons=lesson.objects.filter(garten=KG).all()
    stories=Story.objects.filter(garten=KG).all()
    return render(req,'kindergarten/KinderGartenHome.html',{'lessons':lessons,'stories':stories})


@login_required
def Add_HomeWork(req):
    if req.method == 'POST':

        form1=HomeWorkForm(data=req.POST)
        form2=QuestionForm(data=req.POST)

        if form1.is_valid() and form2.is_valid():
            homework=form1.save(commit=False)
            question=form2.save(commit=False)

            teacher=Teacher.objects.filter(username=req.user.username).first()
            garten=Kindergarten.objects.filter(myTeacher=teacher).first()
            
            homework.garten=garten
            homework.save()

            question.homeWork=homework
            question.save()

            messages.success(req,f'The question has been added')
            if 'has_next' not in form2.data:
                return redirect("show_teacher_homeworks")
            else:
                return redirect("Add_Question",HomeWork_Id=homework.id)


    form1=HomeWorkForm()
    form2=QuestionForm()
    return render(req,'kindergarten/add_HomeWork.html',{'form1':form1,'form2':form2})


@login_required
def Add_Question(req,HomeWork_Id):
    if req.method == 'POST':

        form=QuestionForm(data=req.POST)

        if form.is_valid() :
            homework=HomeWork.objects.filter(id=HomeWork_Id).first()
            question=form.save(commit=False)
            question.homeWork=homework
            question.save()

            messages.success(req,f'The qustion has been added')
            if 'has_next' not in form.data:
                return redirect("show_teacher_homeworks")
            else:
                return redirect("Add_Question",HomeWork_Id=homework.id)


    form=QuestionForm()
    return render(req,'kindergarten/add_question.html',{'form':form})

@login_required
def show_teacher_homeworks(req):
    teacher=Teacher.objects.filter(username=req.user.username).first()
    garten=Kindergarten.objects.filter(myTeacher=teacher).first()
    homeworks=HomeWork.objects.filter(garten=garten)
    return render(req,'kindergarten/teacher_Homeworks.html',{'homeworks':homeworks})


@login_required
def show_homework_questions(req,HomeWork_Id):
    homework=HomeWork.objects.filter(id=HomeWork_Id).first()
    questions=Question.objects.filter(homeWork=homework)
    return render(req,'kindergarten/homework.html',{'homework':homework,'questions':questions})

@login_required
def show_homework_questions_for_kid(req,HomeWork_Id):
    homework=HomeWork.objects.filter(id=HomeWork_Id).first()
    questions=Question.objects.filter(homeWork=homework)
    return render(req,'kindergarten/Solve_homework.html',{'homework':homework,'questions':questions})


@login_required
def show_homeworks_for_kid(req):
    kid=Kid.objects.filter(username=req.user.username).first()
    garten=kid.garten
    homeworks=HomeWork.objects.filter(garten=garten)
    return render(req,'kindergarten/kid_Homeworks.html',{'homeworks':homeworks})


@login_required
def solve_homework(req,HomeWork_Id):
    homework=HomeWork.objects.filter(id=HomeWork_Id).first()
    questions=Question.objects.filter(homeWork=homework)
    count=0
    for q in questions:
        ans = req.POST.getlist(str(q.id))
        right=q.answer
        options=[q.option1,q.option2,q.option3,q.option4]
        if len(ans) == 1 :
            if ans[0] == options[int(right)-1] :
                count+=1

    grade=(count/len(questions))*100
    messages.success(req,f'Your grade are {grade}')
    return redirect("show_homeworks_for_kid")

@login_required
def watch_lesson(req,id):
    l=lesson.objects.filter(id=id).first()
    kid = Kid.objects.filter(username=req.user.username).first()
    temp = View.objects.filter(Lesson=l,kid=kid).first()
    if not temp:
        view = View(Lesson=l,kid=kid)
        view.save()

    return render(req,'kindergarten/watch_lesson.html',{'lesson':l})


@login_required  
def kindergarten_activites(req):
    kid=Kid.objects.filter(username=req.user.username).first()
    KG=kid.garten
    lessons=lesson.objects.filter(garten=KG)
    return render(req,'kindergarten/kindergarte_aktivites.html',{'lessons':lessons})