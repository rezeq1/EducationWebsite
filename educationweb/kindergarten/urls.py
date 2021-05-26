from django.urls import path

from .views import *

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
    path('show_homework_questions_for_kid/<int:HomeWork_Id>/',show_homework_questions_for_kid,name="show_homework_questions_for_kid"),
    path('solve_homework/<int:HomeWork_Id>/',solve_homework,name="solve_homework"),
    path('show_homeworks_for_kid/',show_homeworks_for_kid,name="show_homeworks_for_kid"),
    path('watch_lesson/<int:id>/',watch_lesson,name="watch_lesson"),
    path('kindergarten_activites/',kindergarten_activites,name='kindergarten_activites'),
    path('Get_Kid_stories/',Get_Kid_stories,name='Get_Kid_stories'),
    path('Show_story_for_kid/<int:id>/',Show_story_for_kid,name="Show_story_for_kid"),
    
    


]

