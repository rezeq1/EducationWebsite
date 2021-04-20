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
from .forms import LessonForm
# Create your views here.

def add_lesson(req):
    if req.method == 'POST':
        form=LessonForm(req.POST)
        lesson=form.save(commit=False)
        print(lesson.video_file)
        if form.is_valid() and ( lesson.desc):
            messages.success(req,f'The lesson has been uploaded')
            return redirect("add_lesson")
    else:

        form=LessonForm()
    return render(req,'kindergarten/add_lesson.html',{'form':form})

