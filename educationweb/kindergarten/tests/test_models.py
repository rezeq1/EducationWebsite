from django.test import TestCase
from ..models import *

class lessonTest(TestCase):
    def test_lesson_creation(self):
        l=lesson(title='test',desc='this is only a test')
        self.assertTrue(isinstance(l,lesson))
class StoryTest(TestCase):
    def test_story_creation(self):
        story=Story(title='test')
        self.assertTrue(isinstance(story,Story))

class StoryPageTest(TestCase):
    def test_story_Page_creation(self):
        story=StoryPage()
        self.assertTrue(isinstance(story,StoryPage))
