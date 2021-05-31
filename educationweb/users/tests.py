from django.test import TestCase,Client
from .models import *
from .auth import *
from .Kindergarten_methods import *
from .views import *
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

    def test_Change_Kindergarten_1(self):
        a=auth()
        p=Parent(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        a.parent_register(p)
        kid=Kid(password='123456',username='kidtest',first_name='user',age=5,last_name='last',email='email@email')
        kid.myParent=p
        a.kid_register(kid)
        t=Teacher(password='123456',username='teacer',first_name='user',last_name='last',email='email@email')
        t2=Teacher(password='123456',username='teacer2',first_name='user',last_name='last',email='email1@email')
        a.teacher_register(t)
        a.teacher_register(t2)
        Kk=Kindergarten(name='test',seatLimit=20)
        Kk2=Kindergarten(name='test2',seatLimit=20)
        k=Kindergarten_methods(Kk)
        k.create(t)
        k.add_kid(kid)
        k2=Kindergarten_methods(Kk2)
        k2.create(t2)
        k2.Change_Kindergarten(kid)
        self.assertTrue(kid.garten==Kk2)

    def test_Change_Kindergarten_2(self):
        a=auth()
        p=Parent(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        kid=Kid(password='123456',username='kidtest',first_name='user',age=5,last_name='last',email='email@email')
        t1=Teacher(password='123456',username='teacher1',first_name='user1',last_name='last1',email='email1@email')
        t2=Teacher(password='123456',username='teacher2',first_name='user2',last_name='last2',email='email2@email')
        Kk1=Kindergarten(name='test1',seatLimit=20)
        Kk2=Kindergarten(name='test2',seatLimit=20)

        a.parent_register(p)
        kid.myParent=p
        a.kid_register(kid)
        a.teacher_register(t1)
        a.teacher_register(t2)
        k1=Kindergarten_methods(Kk1)
        k1.create(t1)
        k1.add_kid(kid)
        k2=Kindergarten_methods(Kk2)
        k2.create(t2)
        k2.Change_Kindergarten(kid)

        self.assertTrue(kid.garten==Kk2)
    
    def test_kick_kid_1(self):
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
        k.Kick_From_Kindergarten(kid)
        self.assertIsNotNone(kid.garten)

    def test_kick_kid_2(self):
        a=auth()

        p=Parent(password='a213sf',username='12as3dsf',first_name='us12er',last_name='last',email='emaasil@email')
        kid=Kid(password='123',username='kidsdftest',first_name='uasdser',age=5,last_name='laa1st',email='emsail@aas')
        t=Teacher(password='dsf',username='sdf24',first_name='user',last_name='last',email='eddmail@asd')
        Kk=Kindergarten(name='tesdfst',seatLimit=20)

        a.parent_register(p)
        kid.myParent=p
        a.kid_register(kid)
        a.teacher_register(t)
        k=Kindergarten_methods(Kk)
        k.create(t)
        k.add_kid(kid)
        k.Kick_From_Kindergarten(kid)

        self.assertIsNotNone(kid.garten)

    def test_add_rate(self):
        a=auth()

        p=Parent(password='a213sf',username='12as3dsf',first_name='us12er',last_name='last',email='emaasil@email')
        kid=Kid(password='123',username='kidsdftest',first_name='uasdser',age=5,last_name='laa1st',email='emsail@aas')
        t=Teacher(password='dsf',username='sdf24',first_name='user',last_name='last',email='eddmail@asd')
        Kk=Kindergarten(name='tesdfst',seatLimit=20)

        a.parent_register(p)
        kid.myParent=p
        a.kid_register(kid)
        a.teacher_register(t)
        k=Kindergarten_methods(Kk)
        k.create(t)
        k.add_kid(kid)

        rate=k.add_rate(10,kid)


        self.assertIsNotNone(rate)

    

    def test_kid_message_board(self):
        k=Kid(password='123456',username='kidTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='kidTest', password='123456')

        res=c.get(f'/home/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, home)
    
    def test_teacher_message_board(self):
        t=Teacher(password='123456',username='teacer',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='teacer', password='123456')

        res=c.get(f'/home/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, home)


    def test_rate(self):
        rate=Rate()
        self.assertTrue(isinstance(rate,Rate))
