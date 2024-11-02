# The following lines (2-5) are used to import required modules and functions to be able to test the calculator.
import unittest # The module for creating and running tests
from unittest.mock import patch # Used to replace input and output functions to simulate user interaction and store the output
from io import StringIO # Acts as a file to store printed output, which will be used by the test to verify what the calculator would have printed.
from SampleCalc import main  # Importing the main function of the calculator script which will be tested


class TestSampleCalc(unittest.TestCase):

    #The setUp method is used to store the printed output during the test
    def setUp(self):
        # Create a StringIO object to capture the printed output
        self.output_stream = StringIO()
        # Redirecting sys.stdout to StringIO to store the printed output
        self.patcher = patch('sys.stdout', new=self.output_stream)
        # Start the patcher to begin capturing the output
        self.patcher.start()

    # The tearDown method is used to stop the patch after each test case
    def tearDown(self):
        # Stop the patcher to return sys.stdout to its original state
        self.patcher.stop()



    # Test for addition operation
    @patch('builtins.input', side_effect=['5', '+', '3'])
    # `@patch` is a decorator from `unittest.mock` that is used to replace something with a mock during a test.
    # In this code, `@patch('builtins.input', side_effect=...)` replaces the `input` function with a mock that automatically provides the specified values.
    # This way, we can simulate user input without having to manually type it during the test.
    def test_addition(self, mock_input):
        # Mock user inputs: first number as 5, operator as '+', and second number as 3
        # Run the main calculator function with mocked inputs
        main()
        # Verify that the output contains the correct result for addition
        self.assertIn("The result is: 8.0", self.output_stream.getvalue())

    # Test for subtraction operation
    @patch('builtins.input', side_effect=['10', '-', '4'])
    def test_subtraction(self, mock_input):
        # Mock user inputs: first number as 10, operator as '-', and second number as 4
        # Run the main calculator function with mocked inputs
        main()
        # Verify that the output contains the correct result for subtraction
        self.assertIn("The result is: 6.0", self.output_stream.getvalue())

    # Test for multiplication operation
    @patch('builtins.input', side_effect=['6', '*', '7'])
    def test_multiplication(self, mock_input):
        # Mock user inputs: first number as 6, operator as '*', and second number as 7
        # Run the main calculator function with mocked inputs
        main()
        # Verify that the output contains the correct result for multiplication
        self.assertIn("The result is: 42.0", self.output_stream.getvalue())

    # Test for division operation
    @patch('builtins.input', side_effect=['20', '/', '5'])
    def test_division(self, mock_input):
        # Mock user inputs: first number as 20, operator as '/', and second number as 5
        # Run the main calculator function with mocked inputs
        main()
        # Verify that the output contains the correct result for division
        self.assertIn("The result is: 4.0", self.output_stream.getvalue())

    # Test for handling an invalid operator input
    @patch('builtins.input', side_effect=['10', '%', '3', '+', '3'])
    def test_invalid_operator(self, mock_input):
        # Mock user inputs: first number as 10, invalid operator as '%', then retry with operator as '+' and second number as 3
        # Run the main calculator function with mocked inputs including an invalid operator
        main()
        # Verify that the output contains an invalid operator message indicating the user must retry
        self.assertIn("Invalid Operator", self.output_stream.getvalue())

    # Test for division by zero scenario
    @patch('builtins.input', side_effect=['10', '/', '0'])
    def test_division_by_zero(self, mock_input):
        # Mock user inputs: first number as 10, operator as '/', and second number as 0 to simulate division by zero
        # Run the main calculator function with mocked inputs including division by zero
        main()
        # Verify that the output contains the error message for division by zero to inform the user
        self.assertIn("Cannot divide by zero", self.output_stream.getvalue())


# Main block to execute the tests
if __name__ == '__main__':
    unittest.main()
