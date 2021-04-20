from .models import Quiz
class garten:
    def add_lesson(self,lesson,kinderGarten):
        quiz=Quiz()
        quiz.save()
        lesson.garten=kinderGarten
        lesson.quiz=quiz
        lesson.save()
        return quiz
    
    def addQustion(self,qustion,quiz):
        qustion.quiz=quiz
        qustion.save()
    
