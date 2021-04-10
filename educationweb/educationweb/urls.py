"""educationweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('delete_kid/<str:username>/',user_views.delete_kid,name='delete_kid'),
    path('admin/', admin.site.urls),
    path('parent_register/',user_views.parent_register,name='parent_register'),
    path('teacher_register/',user_views.teacher_register,name='teacher_register'),
    path('kid_register/',user_views.kid_register,name='kid_register'),
    path('show_kids/',user_views.show_kids,name='show_kids'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('login_teacher',auth_views.LoginView.as_view(template_name='users/login_teacher.html'),name='login_teacher'),  
    path('login_kid',auth_views.LoginView.as_view(template_name='users/login.html'),name='login_kid'),  
    path('home/',user_views.home,name='home'),
    path('Register_To_Kindergarten/<str:username>/',user_views.Register_To_Kindergarten,name='Register_To_Kindergarten'),
    path('home/delete_parent/',user_views.delete_parent,name='delete_parent'),
    path('home/delete_teacher/',user_views.delete_teacher,name='delete_teacher'),
    path('Kindergarten_register/',user_views.Kindergarten_register,name='Kindergarten_register'),

    
]
