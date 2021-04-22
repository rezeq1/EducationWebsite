from ..views import add_lesson,add_Qustion,show_teacher_lessons,lesson_info
from django.test import TestCase,Client
from users.models import *
from ..models import Quiz



class ViewsTestCase(TestCase):
    def test_add_lesson(self):
        t=Teacher(password='123456',username='teacer',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='teacer', password='123456')
        res=c.get('/add_lesson')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, add_lesson)
    
    def test_add_Qustion(self):
        t=Teacher(password='123456',username='teacer',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='teacer', password='123456')
        quiz=Quiz()
        quiz.save()
        res=c.get(f'/add_qustion/{quiz.id}/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, add_Qustion)
    
    def test_lesson_info(self):
        t=Teacher(password='123456',username='teacer',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='teacer', password='123456')
        quiz=Quiz()
        quiz.save()
        res=c.get(f'/lesson_info/{quiz.id}/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, lesson_info)
    
    def test_show_teacher_lessons(self):
        t=Teacher(password='123456',username='teacer',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='teacer', password='123456')
        quiz=Quiz()
        quiz.save()
        res=c.get(f'/show_teacher_lessons')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, show_teacher_lessons)

