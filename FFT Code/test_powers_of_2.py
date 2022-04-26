import unittest
from random import randint, uniform

class TestPowersOf2(unittest.TestCase):
    powers_of_2 = [2 ** n for n in range(100)]
    random_natural_numbers = [randint(1, max(powers_of_2)) for _ in range(100)]

    def test_natural_numbers(self):
        self.assertEqual(True, False)

    def test_negative(self):

    def test_zero(self):

    def test_positive_floats(self):

if __name__ == '__main__':
    unittest.main()
