from .models import *
class garten:
    
    def add_lesson(self,lesson,kinderGarten):
        lesson.garten=kinderGarten
        lesson.save()

    def addQuestion(self,question,homework):
        question.homeWork=homework
        question.save()

    def add_Story(self,story,kinderGarten):
        story.garten=kinderGarten
        story.save()

    def add_Page(self,Page,story):
        Page.story=story
        Page.save()

    
