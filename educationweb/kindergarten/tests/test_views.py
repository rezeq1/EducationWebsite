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
    
    def test_get_kid_stories(self):
        k=Kid(password='123456',username='kidTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='kidTest', password='123456')

        res=c.get(f'/Get_Kid_stories/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, Get_Kid_stories)
    
    def test_show_story_for_kid(self):
        k=Kid(password='123456',username='kidTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='kidTest', password='123456')

        res=c.get(f'/Show_story_for_kid/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, Show_story_for_kid)
    
    def test_get_kid_homeworks(self):
        k=Kid(password='123456',username='kidTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='kidTest', password='123456')

        res=c.get(f'/show_homeworks_for_kid/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, show_homeworks_for_kid)
    
    def test_kid_solve_homework(self):
        k=Kid(password='123456',username='kidTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='kidTest', password='123456')

        res=c.get(f'/solve_homework/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, solve_homework)
    
    def test_get_teacher_stories(self):
        k=Teacher(password='123456',username='TeacherTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='TeacherTest', password='123456')

        res=c.get(f'/KinderGartenHome/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, KinderGartenHome)
    
    def test_show_story_for_teacher(self):
        k=Teacher(password='123456',username='TeacherTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='TeacherTest', password='123456')

        res=c.get(f'/story_info/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, story_info)
        
    
    def test_show_homework_info_for_teacher(self):
        k=Teacher(password='123456',username='TeacherTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='TeacherTest', password='123456')

        res=c.get(f'/show_homework_questions/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, show_homework_questions)
    
    
    def test_teacher_add_story(self):
        k=Teacher(password='123456',username='TeacherTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='TeacherTest', password='123456')

        res=c.get(f'/add_story/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, add_story)
    

    def test_teacher_add_lesson(self):
        k=Teacher(password='123456',username='TeacherTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='TeacherTest', password='123456')

        res=c.get(f'/add_lesson/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, add_lesson)
    
    
    def test_kid_watch_lesson(self):
        k=Teacher(password='123456',username='TeacherTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='TeacherTest', password='123456')

        res=c.get(f'/watch_lesson/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, watch_lesson)
    
    def test_teacher_add_questions_to_homework(self):
        k=Teacher(password='123456',username='TeacherTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='TeacherTest', password='123456')

        res=c.get(f'/Add_Question/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, Add_Question)
    
    def test_teacher_add_pages_to_story(self):
        k=Teacher(password='123456',username='TeacherTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='TeacherTest', password='123456')

        res=c.get(f'/add_Page/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, add_Page)
    
        
    def test_show_homework_questions_for_kid(self):
        k=Kid(password='123456',username='kidTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='kidTest', password='123456')

        res=c.get(f'/show_homework_questions_for_kid/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, show_homework_questions_for_kid)
    

    def test_show_homework_questions_for_teacher(self):
        k=Teacher(password='123456',username='TeacherTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='TeacherTest', password='123456')

        res=c.get(f'/show_homework_questions/1/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, show_homework_questions)
    
         
    def test_kindergarten_activites(self):
        k=Kid(password='123456',username='kidTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='kidTest', password='123456')

        res=c.get(f'/kindergarten_activites/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, kindergarten_activites)

    