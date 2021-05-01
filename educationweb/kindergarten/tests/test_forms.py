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

