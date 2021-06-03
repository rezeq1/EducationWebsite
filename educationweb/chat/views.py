from django.core.checks import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from users.models import *
from .models import *
from django.db.models import Q

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'chat_id': room_name,
        'user':request.user
    })


# Create your views here.
@login_required
def get_chat(req,chat_id):
    chat=Chat.objects.filter(id=chat_id).first()
    messages=chat.messages.all()
    return render(req,'chat/room.html',{

        'chat_id':chat_id,
        'chat_messages':messages
    })

class inpox:
    
    def __init__(self,chatid,chatname,unread):
        self.chatid=chatid
        self.chatname=chatname
        self.unread=unread

def get_chats(req):
    chats=req.user.chats.all()
    parent=Parent.objects.filter(username=req.user.username).first()
    user=req.user
    chatss=[]
    for i in chats:
        if (parent):
            chatName=i.garten.name
        else:
            p=i.participants.filter(~Q(id=req.user.id)).first()
            chatName=p.username
        chatss.append( inpox(i.id,chatName,0))
    return render(req,'chat/chats.html',{
        'chats':chatss
    })
    

def parent_contact(req,id):
    teacher=Teacher.objects.filter(id=id).first()
    g=Kindergarten.objects.filter(myTeacher=teacher).first()
    chats=req.user.chats.all()
    allreadyChating=False
    chatid=None
    for i in chats:
        p=i.participants.filter(~Q(id=teacher.id)).first()
        if p:
            return redirect('chat', chat_id=i.id)
    if not allreadyChating:
        chat=Chat(garten=g)
        chat.save()
        chat.participants.add(teacher)
        chat.participants.add(req.user)
        chatid=chat.id
    return render(req,'chat/room.html',{
        'chat_id':chatid
    })

def get_kids_teachers(req):
    kids=Kid.objects.filter(myParent=req.user).all()
    teacers=[x.garten.myTeacher for x in kids]
    return render(req,"chat/kids_teachers.html",{
        "teacers":teacers
    })

