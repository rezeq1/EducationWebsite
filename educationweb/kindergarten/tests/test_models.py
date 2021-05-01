from django.test import TestCase
from ..models import *

class lessonTest(TestCase):
    def test_lesson_creation(self):
        l=lesson(title='test',desc='this is only a test')
        self.assertTrue(isinstance(l,lesson))
