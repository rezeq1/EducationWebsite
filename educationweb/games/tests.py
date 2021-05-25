from .views import *
from django.test import TestCase,Client
from users.models import *



class ViewsTestCase(TestCase):

    def test_kid_Play_game(self):
        k=Kid(password='123456',username='kidTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='kidTest', password='123456')

        res=c.get(f'/Play_game/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, Play_game)
    
    def test_kid_Play_numbers_memory_game(self):
        k=Kid(password='123456',username='kidTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='kidTest', password='123456')

        res=c.get(f'/numbers_memory_game/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, numbers_memory_game)
    
    def test_kid_Play_animals_memory_game(self):
        k=Kid(password='123456',username='kidTest',first_name='user',last_name='last',email='email@email')
        c = Client()
        c.login(username='kidTest', password='123456')

        res=c.get(f'/animals_memory_game/')
        self.assertEqual(res.status_code,302)
        self.assertEqual(res.resolver_match.func, animals_memory_game)