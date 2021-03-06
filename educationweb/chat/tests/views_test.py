from django.test import TestCase, tag
from django.urls import reverse
from users.models import *
from ..models import *


class ViewsTestCase(TestCase):

    def test_teacher_inpox(self):
        t=Teacher(password='123456',username='teacer',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='teacer', password='123456')

        res=c.get(f'/teacher_inpox/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, lesson_info)
    
    def test_parent_inpox(self):
        t=Parent(password='123456',username='teacer',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='teacer', password='123456')

        res=c.get(f'/parent_inpox/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, lesson_info)
    
    def test_chat(self):
        k=Kid(password='123456',username='kidTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='kidTest', password='123456')

        res=c.get(f'/chats/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, Get_Kid_stories)