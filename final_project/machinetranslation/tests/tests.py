import unittest
from translator import englishToFrench
from translator import frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_null_input_f2e(self):
        """ Test case for null imput for frenchToEnglish """
        result = frenchToEnglish("")
        expected = ""
        self.assertEqual(result, expected)
    
    def test_null_input_e2f(self):
        """ Test case for null imput for englistToFrench """
        result = englishToFrench("")
        expected = ""
        self.assertEqual(result, expected)

    def test_bonjour_hello_f2e(self):
        """ Test case for Bonjour and Hello input for frenchToEnglish """
        result = frenchToEnglish("Bonjour")
        expected = "Hello"
        self.assertEqual(result, expected)

    def test_hello_bonjour_e2f(self):
        """ Test case for Hello and Bonjour input for englishToFrench """
        result = englishToFrench("Hello")
        expected = "Bonjour"
        self.assertEqual(result, expected)
    
if __name__ == "__main__":
    unittest.main()