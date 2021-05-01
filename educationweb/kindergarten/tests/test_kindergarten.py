from ..kindergarten_class import *
from users.models import Kindergarten,Teacher
from ..models import *
from django.test import TestCase

class gartenTestCase(TestCase):

    def test_add_lesson(self):
        g=garten()
        l=lesson(title='test',desc='this is only a test')
        t=Teacher(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        t.save()
        Kk=Kindergarten(name='test',seatLimit=20,myTeacher=t)
        Kk.save()
        g.add_lesson(lesson=l,kinderGarten=Kk)
        self.assertIsNotNone(l)
    
        
    def test_add_HomeWork(self):
        t=Teacher(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        t.save()
        Kk=Kindergarten(name='test',seatLimit=20,myTeacher=t)
        Kk.save()
        g=garten()
        HW=g.addHomeWork("Test",10,Kk)
        self.assertIsNotNone(HW)
    
            
    def test_add_Question(self):
        t=Teacher(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        t.save()
        Kk=Kindergarten(name='test',seatLimit=20,myTeacher=t)
        Kk.save()
        g=garten()
        HW=g.addHomeWork("Test",10,Kk)
        q=Question()
        q.question='test'
        q.save()
        g.addQuestion(q,HW)
        self.assertIsNotNone(q.homeWork)
        