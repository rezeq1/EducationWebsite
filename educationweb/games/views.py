from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

# Create your views here.
def animals_memory_game(req):
    if req.method == 'POST':
        html = "<html><body>It is now </body></html>"
        return HttpResponse(html)
    else:
        return render(req,'games/animals.html')

def numbers_memory_game(req):
    if req.method == 'POST':
        html = "<html><body>It is now </body></html>"
        return HttpResponse(html)
    else:
        return render(req,'games/numbers.html')