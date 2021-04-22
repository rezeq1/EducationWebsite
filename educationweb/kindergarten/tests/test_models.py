from django.test import TestCase
from ..models import *

class lessonTest(TestCase):
    def test_lesson_creation(self):
        quiz=Quiz()
        l=lesson(title='test',desc='this is only a test',quiz=quiz)
        self.assertTrue(isinstance(l,lesson))

class QuizTest(TestCase):
    def test_Quiz_creation(self):
        quiz=Quiz()
        self.assertTrue(isinstance(quiz,Quiz))
    
class QustionTest(TestCase):
    def test_Qustion_creation(self):
        q=Qustion()
        quiz=Quiz()
        q=Qustion(qustion='test?',answer1='1',answer2='1',answer3='1',answer4='1',rightAnswer='2',quiz=quiz)
        self.assertTrue(isinstance(q,Qustion))
