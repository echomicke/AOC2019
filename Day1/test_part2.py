import unittest
import part2 as pt2

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.example_input = [14, 1969, 100756]
    
    def test_modules_fuel_requirements(self):
        expected_sum = 51314
        result = pt2.Total_required_fuel(self.example_input)

        self.assertEqual(expected_sum, result)