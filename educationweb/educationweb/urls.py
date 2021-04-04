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
    path('admin/', admin.site.urls),
    path('parent_register/',user_views.parent_register,name='parent_register'),
    path('teacher_register/',user_views.teacher_register,name='teacher_register'),
<<<<<<< HEAD
    path('',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'), 
    path('home/',user_views.home,name='home'),
    
=======
    path('',user_views.home,name='home'),
>>>>>>> 937088d18948e906995ab3bf33b78af196b8d814
]
