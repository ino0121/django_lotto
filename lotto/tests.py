from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNubersTestCase(TestCase):
    def test_geneate(self):
        g = GuessNumbers(name='Test numbers', text='selected number')
        g.generate()
        print(g.update_date)
        print(g.lottos)

        self.assertTrue(len(g.lottos) > 20)
