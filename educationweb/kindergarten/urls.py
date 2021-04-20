from django.urls import path

from .views import add_lesson,show_teacher_lessons,lesson_info,add_Qustion

urlpatterns = [
    path('add_lesson',add_lesson,name="add_lesson"),
    path('show_teacher_lessons',show_teacher_lessons,name="teacher_lessons"),
    path('lesson_info/<int:id>/',lesson_info,name="lesson_info"),
    path('add_qustion/<int:id>/',add_Qustion,name="add_qustion"),


]

