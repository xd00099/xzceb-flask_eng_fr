import unittest
from ../translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_en_to_fr(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    
    def test_fr_to_en(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()