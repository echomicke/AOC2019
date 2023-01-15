import unittest

class TestStringMethods(unittest.TestCase):

    def test_fuel_amount(self):
        mass = 1969
        expected_result = 654
        result = Fuel_required(mass)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()