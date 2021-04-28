from django.test import TestCase,Client
from .models import *
from .auth import *
from .Kindergarten_methods import *
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
    
    def test_parent_login(self):
        client=Client()
        res=client.get('/')
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
    
    def test_remove_teacher(self):
        a=auth()
        p=Teacher(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        a.teacher_register(p)
        a.delete_Teacher(p)
        deletedP=Teacher.objects.filter(username='username').first()
        self.assertIsNone(deletedP)

    def test_register_kid(self):
        a=auth()
        p=Parent(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        a.parent_register(p)
        k=Kid(password='123456',username='kidtest',first_name='user',age=5,last_name='last',email='email@email')
        k.myParent=p
        a.kid_register(k)
        Kregisterd=Kid.objects.filter(username='kidtest').first()
        self.assertIsNotNone(Kregisterd)
    
    def test_remove_kid(self):
        a=auth()
        p=Parent(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        a.parent_register(p)
        k=Kid(password='123456',username='kidtest',first_name='user',age=5,last_name='last',email='email@email')
        k.myParent=p
        a.kid_register(k)
        a.delete_kid(k)
        Kregisterd=Kid.objects.filter(username='kidtest').first()
        self.assertIsNone(Kregisterd)

    def test_register_kindergarten(self):
        a=auth()
        t=Teacher(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        a.teacher_register(t)
        Kk=Kindergarten(name='test',seatLimit=20)
        k=Kindergarten_methods(Kk)
        k.create(t)
        kregisterd=Kindergarten.objects.filter(name='test').first()
        self.assertIsNotNone(kregisterd)
    
    def test_add_kid(self):
        a=auth()
        p=Parent(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        a.parent_register(p)
        kid=Kid(password='123456',username='kidtest',first_name='user',age=5,last_name='last',email='email@email')
        kid.myParent=p
        a.kid_register(kid)
        t=Teacher(password='123456',username='teacer',first_name='user',last_name='last',email='email@email')
        a.teacher_register(t)
        Kk=Kindergarten(name='test',seatLimit=20)
        k=Kindergarten_methods(Kk)
        k.create(t)
        k.add_kid(kid)
        garten=kid.garten
        self.assertIsNotNone(garten)
    
    def test_parent_change_password(self):
        parent=Parent(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        a=auth()
        a.change_password('123456','abcdef',parent)
        self.assertFalse(parent.check_password('abcdef'))

    def test_kid_change_password(self):
        a=auth()
        p=Parent(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        a.parent_register(p)
        k=Kid(password='123456',username='kidtest',first_name='user',age=5,last_name='last',email='email@email')
        k.myParent=p
        a.kid_register(k)
        a.change_password('123456','abcdef',k)
        self.assertFalse(k.check_password('abcdef'))

    


    







    
