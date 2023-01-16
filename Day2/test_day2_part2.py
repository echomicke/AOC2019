import unittest
import day2_part2 as pt2

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.example_input = [1, 1, 1, 4, 99, 5, 6, 0, 99]

    def test_process_intcode(self):
        expected_value = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        result = pt2.process_intcode(self.example_input)

        self.assertEqual(expected_value, result)
    
    def test_find_noun_verb(self):
        target_output = 30
        result = pt2.find_Noun_verb(self.example_input, target_output)
        self.assertEqual(result, 0)