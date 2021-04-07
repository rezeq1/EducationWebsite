from django.test import TestCase
from .models import *
from .auth import *
# Create your tests here.
class AuthTestCase(TestCase):
   

    def test_parent_register(self):
        a=auth()
        p=Parent(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        a.parent_register(p)
        pregusterd=Parent.objects.filter(username='username').first()
        p.delete()
        self.assertIsNotNone(pregusterd)

    def test_teacher_register(self):
        a=auth()
        t=Teacher(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        a.teacher_register(t)
        Tregisterd=Teacher.objects.filter(username='username').first()
        t.delete()
        print('hhhhhhhh')
        self.assertIsNone(Tregisterd)