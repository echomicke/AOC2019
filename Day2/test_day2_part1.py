import unittest
import day2_part1 as pt1

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.example_input = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    

    def test_pre_run(self):
        expected_value = [1, 12, 2, 4, 99, 5, 6, 0, 99]
        result = pt1.pre_run(self.example_input)

        self.assertEqual(expected_value, result)