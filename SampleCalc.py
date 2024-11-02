class Calculator:
    # Method for adding 2 numbers
    def add(self, a, b):
        return a + b

    # Method for subtracting 2 numbers
    def subtract(self, a, b):
        return a-b

    # Method for multiplying 2 numbers
    def multiply(self, a, b):
        return a * b

    # Method for dividing 2 numbers
    def divide(self, a ,b):
        #The below is an error handling technique for dividing by zero
        if b==0:
            # If the user enters 0 an error will be expected
            raise ValueError("Cannot divide by zero")
            # raise is used instead of except to signal an error condition.
            # This allows the calling function how to handle the error
        return a/b


def main():
    success = False # The variable success is used as an indicator to validate the operator chosen
    result = 0

    print("----Calculator----")

    # The section below requests the first number from the user
    try:
        num1 = float(input("Enter first number:"))
    # If a user where to input a value which is not a number it will generate an error
    # and an error message will be displayed
    except ValueError:
        print("Invalid Input! Please enter a number.")
        return # If an error is generated the program is exited to prevent further errors

    # The section below requests an operator from the user
    while not success:
        operator = input("Enter an operator (+, - , *, /): ")
        # The if-else statement below validates that the operaotor is valid
        if operator in ['+', '-', '*', '/']:
            success = True
        else:
            print("Invalid Operator! Please select a valid operator.") # If an invalid operator is used it will display this message

    # The section below requests the second number from the user
    # and like the first number it is validated through try-except technique
    try:
        num2 = float(input("Enter second number:"))
    except ValueError:
        print("Invalid Input! Please enter a number.")
        return

    # The following is an if-elif statement which acts similar to
    # a switch in other programming languages.
    calc = Calculator()
    # The if-elif statements check what type of operator the user inputted
    # and enters the 2 numbers requested as parameters into the operator's method
    try:
        if operator == '+':
            result = calc.add(num1, num2)
        elif operator == '-':
            result = calc.subtract(num1, num2)
        elif operator == '*':
            result = calc.multiply(num1, num2)
        elif operator == '/':
            result = calc.divide(num1, num2)
    except ValueError as x:
        #This section catches the division by zero method and displays the error message
        print(x)
        return

    #The following displays the result
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()

# Lines 77-78 are used to run the main function if the script is executed directly.
# The condition "if __name__ == \"__main__\":" checks if this file is being run as the main program.
# If true, it calls the main() function to execute the calculator logic. This prevents the main function
# from being executed if the module is imported into another script.


