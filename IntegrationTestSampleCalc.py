import unittest  # Import the unittest module to create and run tests
from SampleCalc import Calculator  # Import the Calculator class from SampleCalc.py


# This class is used to test the integration of multiple methods in the Calculator class
class IntegrationTestSampleCalc(unittest.TestCase):
    # Test method to perform multiple operations in sequence
    def test_combined_operations(self):
        calc = Calculator()  # Create an instance of the Calculator class

        # Perform a sequence of operations: ((5 + 3) * 2) - 4

        # Step 1: Add 5 and 3, should return 8
        result = calc.add(5, 3)  # Call the add method of the calculator with 5 and 3, result should be 8

        # Step 2: Multiply the result (8) by 2, should return 16
        result = calc.multiply(result, 2)  # Call the multiply method with the result (8) and 2, result should be 16

        # Step 3: Subtract 4 from the result (16), should return 12
        result = calc.subtract(result, 4)  # Call the subtract method with the result (16) and 4, result should be 12

        # Check if the final result is as expected (12)
        self.assertEqual(result, 12)  # Assert that the final result is equal to 12


# This block runs the test if the script is executed directly
if __name__ == '__main__':
    unittest.main()  # Run the unittest main method to execute the tests
