from django.urls import path

from .views import add_lesson

urlpatterns = [
    path('add_lesson',add_lesson,name="add_lesson")
]