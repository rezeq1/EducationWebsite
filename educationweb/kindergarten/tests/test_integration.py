from ..views import *
from django.test import TestCase,Client
from users.models import *
from ..models import *



class IntegrationTests(TestCase):
    def test_register_login_kid_show_Stories_show_Specific_Story(self):
        k=Kid(password='123456',username='kidTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='kidTest', password='123456')

        res1=c.get(f'/Get_Kid_stories/')
        self.assertEqual(res1.status_code,302)
        self.assertEqual(res1.resolver_match.func, Get_Kid_stories)

        res2=c.get(f'/Show_story_for_kid/1/')
        self.assertEqual(res2.status_code,302)
        self.assertEqual(res2.resolver_match.func, Show_story_for_kid)

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
    
    def test_register_login_kid_show_homeworks_show_Specific_homework(self):
        k=Kid(password='123456',username='kidTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='kidTest', password='123456')

        res=c.get(f'/show_homeworks_for_kid/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, show_homeworks_for_kid)
    
        res=c.get(f'/show_homework_questions_for_kid/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, show_homework_questions_for_kid)


    def test_register_login_teacher_show_homeworks_add_questions_to_homework(self):
        k=Teacher(password='123456',username='TeacherTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='TeacherTest', password='123456')
        
        res=c.get(f'/Add_Question/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, Add_Question)
    
        res=c.get(f'/show_homework_questions/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, show_homework_questions)
    
    def test_register_login_teacher_add_Stories_add_pages_to_Story(self):
        k=Teacher(password='123456',username='TeacherTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='TeacherTest', password='123456')

        res=c.get(f'/add_story/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, add_story)

        res=c.get(f'/add_Page/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, add_Page)
    
    def test_register_login_kid_show_lessons_watch_lesson(self):
        k=Kid(password='123456',username='kidTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='kidTest', password='123456')

        res=c.get(f'/kindergarten_activites/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, kindergarten_activites)
        
        res=c.get(f'/watch_lesson/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, watch_lesson)
        

    def test_register_login_teacher_add_lesson_show_lessons(self):
        k=Teacher(password='123456',username='TeacherTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='TeacherTest', password='123456')
    
        res=c.get(f'/add_lesson/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, add_lesson)
    
        res=c.get(f'/KinderGartenHome/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, KinderGartenHome)
    