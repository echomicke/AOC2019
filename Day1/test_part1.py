import unittest
import part1 as pt1

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        self.example_input = [12, 14, 1969, 100756]


    def test_fuel_amount(self):
        mass = 1969
        expected_result = 654
        result = pt1.Fuel_required(mass)

        self.assertEqual(expected_result, result)


    def test_sum_of_fuel_required(self):
        expected_result = 34241
        result = pt1.Total_fuel_required(self.example_input)
        
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()