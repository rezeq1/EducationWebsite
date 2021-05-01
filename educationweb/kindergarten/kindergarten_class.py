from .models import *
class garten:
    
    def add_lesson(self,lesson,kinderGarten):
        lesson.garten=kinderGarten
        lesson.save()

    def addQuestion(self,question,homework):
        question.homeWork=homework
        question.save()

    
    def addHomeWork(self,subject,duration,garten):
        HW=HomeWork()
        HW.subject=subject
        HW.duration=duration
        HW.garten=garten
        HW.save()
        return HW

    def show_homeworks_for_teacher(self,teacher):
        garten=Kindergarten.objects.filter(myTeacher=teacher).first()
        homeworks=HomeWork.objects.filter(garten=garten)
        return homeworks

    def show_homeworks_for_kid(self,kid):
        garten=kid.garten
        homeworks=HomeWork.objects.filter(garten=garten)
        return homeworks

    def add_Story(self,story,kinderGarten):
        story.garten=kinderGarten
        story.save()

    def add_Page(self,Page,story):
        Page.story=story
        Page.save()

    
