from ..views import *
from django.test import TestCase,Client
from users.models import *
from ..models import *



class ViewsTestCase(TestCase):
    def test_lesson_info(self):
        t=Teacher(password='123456',username='teacer',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='teacer', password='123456')

        res=c.get(f'/lesson_info/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, lesson_info)
    
