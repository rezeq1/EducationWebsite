from django.test import TestCase,Client
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
        self.assertIsNotNone(Tregisterd)
    
    def test_teacher_login(self):
        client=Client()
        res=client.get('/login_teacher')
        self.assertEqual(res.status_code,200)
    
    def test_kid_login(self):
        client=Client()
        res=client.get('/login_kid')
        self.assertEqual(res.status_code,200)
    
    def test_remove_parent(self):
        a=auth()
        p=Parent(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        a.parent_register(p)
        a.delete_Parent(p)
        deletedP=Parent.objects.filter(username='username').first()
        self.assertIsNone(deletedP)



    
