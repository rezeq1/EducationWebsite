from django.urls import path

from .views import add_lesson,KinderGartenHome,lesson_info,add_Qustion,add_story,add_Page

urlpatterns = [
    path('add_lesson/',add_lesson,name="add_lesson"),
    path('KinderGartenHome',KinderGartenHome,name="KinderGartenHome"),
    path('lesson_info/<int:id>/',lesson_info,name="lesson_info"),
    path('add_qustion/<int:id>/',add_Qustion,name="add_qustion"),
    path('add_story/',add_story,name="add_story"),
    path('add_Page/<int:id>/',add_Page,name="add_page"),
    
    


]

