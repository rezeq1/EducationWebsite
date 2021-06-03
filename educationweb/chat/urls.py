from django.urls import path

from . import views

urlpatterns = [
      path('chat/<int:chat_id>/', views.get_chat, name='chat'),
    path('parent_contact/<int:id>/', views.parent_contact, name='parent_contact'),
    path('get_kids_teachers/', views.get_kids_teachers, name='get_kids_teachers'),
    path('parent_inpox/', views.parent_inpox, name='parent_inpox'),
    path('teacher_inpox/', views.teacher_inpox, name='teacher_inpox'),
]