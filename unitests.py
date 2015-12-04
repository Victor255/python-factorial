import application
import unittest

class FactorialTest(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(application.factorial(5), 120)
        self.assertEqual(application.factorial(2), 2)
        self.assertEqual(application.factorial(7), 5040)

if __name__ == '__main__':
    unittest.main()