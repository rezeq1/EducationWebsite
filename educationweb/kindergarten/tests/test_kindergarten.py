from ..kindergarten_class import *
from users.models import Kindergarten,Teacher
from ..models import *
from django.test import TestCase

class gartenTestCase(TestCase):

    def test_add_lesson(self):
        g=garten()
        quiz=Quiz()
        quiz.save()
        l=lesson(title='test',desc='this is only a test',quiz=quiz)
        t=Teacher(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        t.save()
        Kk=Kindergarten(name='test',seatLimit=20,myTeacher=t)
        Kk.save()
        g.add_lesson(lesson=l,kinderGarten=Kk)
        l=lesson.objects.filter(quiz=quiz)
        self.assertIsNotNone(l)
    

    def test_addQustion(self):
        g=garten()
        quiz=Quiz()
        quiz.save()

        q=Qustion(qustion='test?',answer1='1',answer2='1',answer3='1',answer4='1',rightAnswer='2',quiz=quiz)
        g.addQustion(qustion=q,quiz=quiz)
        l=Qustion.objects.filter(quiz=quiz)
        self.assertIsNotNone(l)

