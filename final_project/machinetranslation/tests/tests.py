import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    
    def test_french_to_english(self):
        result = french_to_english('Bonjour')
        self.assertEqual(result,'Hello')
        result = french_to_english(' ')
        self.assertNotEqual(result,'Hello')

    def test_english_to_french(self):
        result = english_to_french('Hello')
        self.assertEqual(result,'Bonjour')
        result = english_to_french(' ')
        self.assertNotEqual(result,'Bonjour')

if __name__=='__main__':
    unittest.main()

