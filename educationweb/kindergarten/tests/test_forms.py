from ..forms import *
from django.test import TestCase


class LessonFormTestCase(TestCase):
    def test_valid(self):
        data={'title':'test'}
        form=LessonForm(data)
        self.assertTrue(form.is_valid())
    
    def test_invalid(self):
        data={}
        form=LessonForm(data)
        self.assertFalse(form.is_valid())

class QustionFormTestCase(TestCase):
    def test_valid(self):
        data={'qustion':'test?','answer1':'1','answer2':'2','answer3':'2','answer4':'3','rightAnswer':'1'}
        form=QustionForm(data)
        self.assertTrue(form.is_valid())
    
    def test_invalid(self):
        data={'qustion':'test?','answer1':'1','answer2':'2','answer3':'2','answer4':'3','rightAnswer':'5'}
        form=QustionForm(data)
        self.assertFalse(form.is_valid())