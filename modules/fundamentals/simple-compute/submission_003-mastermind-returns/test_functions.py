import unittest
import mastermind
from test_base import captured_io
import sys
from unittest.mock import patch # Patch module: insert on user's behalf
from io import StringIO


class TestMethods(unittest.TestCase):

    def test_create_code_list(self):
        """
        Test that it can create a 4-digit list.
        """
        for _ in range(100):
            code = mastermind.create_code()
            code_s = set(code) # A set does not allow duplicates.
            self.assertEqual(len(code_s), 4)


    def test_code_digit_range(self):
        """
        Test that its numbers are within range of 1 to 8.
        """
        code = mastermind.create_code()
        is_in_range = True
        for i in range(100):
            for j in range(4):
                if code[j] < 1 or code[j] > 8:
                    is_in_range = False
                    self.assertTrue(is_in_range, "Digits not within range.")
                else:
                    is_in_range = True
        self.assertTrue(is_in_range)

    # def test_code_correctness(self):
    #     """
    #     Test that the entered numbers are correct.
    #     """
    #     correct = False
    #     correct_digits_and_position = 0
    #     turns = 11
    #     # mastermind.check_correctness evaluates to True or False
    #     if correct_digits_and_position > 4 or correct_digits_and_position < 4:
    #         self.assertFalse(mastermind.check_correctness(correct_digits_and_position, turns, correct))
    #     elif correct_digits_and_position == 4:
    #         self.assertTrue(mastermind.check_correctness(correct_digits_and_position, turns, correct))


    def test_check_correction(self):
        with captured_io(''):
            self.assertEqual(mastermind.check_correctness(1,4,True), True)
            
    def test_get_input(self):
        with captured_io(StringIO("0000\n9999\naaaa\n123\n1a2b\n12345\n1234")):
            self.assertEqual(len(mastermind.get_user_input()), 4)
                
    def test_correct_digits(self):
        code = [1,2,3,4]
        with captured_io(StringIO("4321\n1423\n3214\n2134\n1234")):
            self.assertEqual(mastermind.take_turn(code), (0, 4))
            self.assertEqual(mastermind.take_turn(code), (1, 3))
            self.assertEqual(mastermind.take_turn(code), (2, 2))
            self.assertEqual(mastermind.take_turn(code), (2, 2))
            self.assertEqual(mastermind.take_turn(code), (4, 0))


    # @patch("sys.stdin", StringIO("123\n1234\n")) # Patch the sys.stdin with a string
    # def test_get_user_input(self):
    #     """
    #     Test that the system output matches the output that we are expecting.
    #     """
    #     sys_o_put = sys.stdout # Hold original system output
    #     o_put = StringIO() # Convert the output to a string
    #     sys.stdout = o_put # The converted string is assigned to sys.stdout
    #     mastermind.get_user_input() # Run the function
    #     i_put = o_put.getvalue() # Get the value of the converted string
    #     # Compare the actual, saved output to what we expect
    #     self.assertEqual(i_put, """Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: """)


if __name__ == '__main__':
    unittest.main()