from ..views import *
from django.test import TestCase,Client
from users.models import *
from ..models import *



class IntegrationTests(TestCase):
   
    def test_register_login_teacher_show_Stories_show_Specific_Story(self):
        k=Teacher(password='123456',username='TeacherTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='TeacherTest', password='123456')

        res=c.get(f'/KinderGartenHome/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, KinderGartenHome)

        res=c.get(f'/story_info/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, story_info)
    
    