from django.urls import path

from .views import add_lesson,KinderGartenHome,lesson_info,add_story,add_Page,story_info

urlpatterns = [
    path('add_lesson/',add_lesson,name="add_lesson"),
    path('KinderGartenHome/',KinderGartenHome,name="KinderGartenHome"),
    path('show_teacher_homeworks',show_teacher_homeworks,name="show_teacher_homeworks"),
    path('lesson_info/<int:id>/',lesson_info,name="lesson_info"),
    path('story_info/<int:id>/',story_info,name="story_info"),
    path('Add_HomeWork',Add_HomeWork,name="Add_HomeWork"),
    path('add_story/',add_story,name="add_story"),
    path('add_Page/<int:id>/',add_Page,name="add_page"),
    path('Add_Question/<int:HomeWork_Id>/',Add_Question,name="Add_Question"),
    path('show_homework_questions/<int:HomeWork_Id>/',show_homework_questions,name="show_homework_questions"),
    
    


]

