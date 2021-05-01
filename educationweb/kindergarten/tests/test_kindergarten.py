from ..kindergarten_class import *
from users.models import *
from ..models import *
from django.test import TestCase

class gartenTestCase(TestCase):

    def test_add_lesson(self):
        g=garten()
        l=lesson(title='test',desc='this is only a test')
        t=Teacher(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        t.save()
        Kk=Kindergarten(name='test',seatLimit=20,myTeacher=t)
        Kk.save()
        g.add_lesson(lesson=l,kinderGarten=Kk)
        self.assertIsNotNone(l)
    
        
    def test_add_HomeWork(self):
        t=Teacher(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        t.save()
        Kk=Kindergarten(name='test',seatLimit=20,myTeacher=t)
        Kk.save()
        g=garten()
        HW=g.addHomeWork("Test",10,Kk)
        self.assertIsNotNone(HW)
    
            
    def test_add_Question(self):
        t=Teacher(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        t.save()
        Kk=Kindergarten(name='test',seatLimit=20,myTeacher=t)
        Kk.save()
        g=garten()
        HW=g.addHomeWork("Test",10,Kk)
        q=Question()
        q.question='test'
        q.save()
        g.addQuestion(q,HW)
        self.assertIsNotNone(q.homeWork)

            
    def test_show_homeworks_for_teacher(self):
        t=Teacher(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        t.save()
        Kk=Kindergarten(name='test',seatLimit=20,myTeacher=t)
        Kk.save()
        g=garten()
        HW=g.addHomeWork("Test",10,Kk)
        homeworks=g.show_homeworks_for_teacher(t)
        self.assertIsNotNone(homeworks)

    def test_show_homeworks_for_kid(self):
        t=Teacher(password='1356',username='user1name',first_name='user',last_name='last',email='email@email')
        t.save()
        Kk=Kindergarten(name='test',seatLimit=20,myTeacher=t)
        Kk.save()
        g=garten()
        HW=g.addHomeWork("Test",10,Kk)
        p=Parent(password='12456',username='usern3ame',first_name='user',last_name='last',email='email@email')
        p.save()
        kid=Kid(password='11456',username='kidte5st',first_name='user',age=5,last_name='last',email='email@email')
        kid.myParent=p
        kid.garten=Kk
        kid.save()
        homeworks=g.show_homeworks_for_kid(kid)
        self.assertIsNotNone(homeworks)

    def test_kindergarten_activites(self):
        g=garten()
        l=lesson(title='test',desc='this is only a test')
        t=Teacher(password='123456',username='username',first_name='user',last_name='last',email='email@email')
        t.save()
        Kk=Kindergarten(name='test',seatLimit=20,myTeacher=t)
        Kk.save()
        g.add_lesson(lesson=l,kinderGarten=Kk)
        p=Parent(password='12456',username='usern3ame',first_name='user',last_name='last',email='email@email')
        p.save()
        kid=Kid(password='11456',username='kidte5st',first_name='user',age=5,last_name='last',email='email@email')
        kid.myParent=p
        kid.garten=Kk
        kid.save()
        lessons = g.get_kindergarten_activites(kid)
        self.assertIsNotNone(lessons)

    def test_add_grades(self):
        t=Teacher(password='1356',username='user1name',first_name='user',last_name='last',email='email@email')
        t.save()
        Kk=Kindergarten(name='test',seatLimit=20,myTeacher=t)
        Kk.save()
        g=garten()
        HW=g.addHomeWork("Test",10,Kk)
        p=Parent(password='12456',username='usern3ame',first_name='user',last_name='last',email='email@email')
        p.save()
        kid=Kid(password='11456',username='kidte5st',first_name='user',age=5,last_name='last',email='email@email')
        kid.myParent=p
        kid.garten=Kk
        kid.save()
        grades = g.add_grade(kid,HW,100)
        self.assertIsNotNone(grades)
    
    def test_get_grades(self):
        t=Teacher(password='1356',username='user1name',first_name='user',last_name='last',email='email@email')
        t.save()
        Kk=Kindergarten(name='test',seatLimit=20,myTeacher=t)
        Kk.save()
        g=garten()
        HW=g.addHomeWork("Test",10,Kk)
        p=Parent(password='12456',username='usern3ame',first_name='user',last_name='last',email='email@email')
        p.save()
        kid=Kid(password='11456',username='kidte5st',first_name='user',age=5,last_name='last',email='email@email')
        kid.myParent=p
        kid.garten=Kk
        kid.save()
        g.add_grade(kid,HW,100)
        grades = g.get_grade(kid)
        self.assertIsNotNone(grades)
    
