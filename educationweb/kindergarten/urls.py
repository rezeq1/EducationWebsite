from django.urls import path

from .views import add_lesson,KinderGartenHome,lesson_info,add_story,add_Page,story_info

urlpatterns = [
    path('add_lesson/',add_lesson,name="add_lesson"),
    path('KinderGartenHome/',KinderGartenHome,name="KinderGartenHome"),
    path('lesson_info/<int:id>/',lesson_info,name="lesson_info"),
    path('story_info/<int:id>/',story_info,name="story_info"),

    path('add_story/',add_story,name="add_story"),
    path('add_Page/<int:id>/',add_Page,name="add_page"),
    
    


]

