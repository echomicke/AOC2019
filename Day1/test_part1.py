import unittest
import part1 as pt1

class TestStringMethods(unittest.TestCase):

    def test_fuel_amount(self):
        mass = 1969
        expected_result = 654
        result = pt1.Fuel_required(mass)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()