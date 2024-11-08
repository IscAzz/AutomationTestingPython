# The app.py file is a Flask web application that serves as an API for a simple calculator.
# It exposes multiple endpoints (/add, /subtract, /multiply, /divide) that allow users to perform basic arithmetic
# operations by sending HTTP GET requests with parameters (a and b).
# Each endpoint returns the result of the calculation. The application is intended for testing and development purposes,
# providing an easy way to interact with the calculator operations programmatically.
from flask import Flask, request, jsonify  # Import necessary Flask components to create the web server and handle HTTP requests
from SampleCalc import Calculator  # Import the Calculator class from SampleCalc.py to use its methods

app = Flask(__name__)  # Create a Flask app instance, which acts as the web server
calc = Calculator()  # Create an instance of the Calculator class to perform operations

# Define a route for addition operation
@app.route('/add', methods=['GET'])  # Specify the route for the addition operation and allow only GET requests
def add():
    a = float(request.args.get('a'))  # Get the 'a' parameter from the URL query string, convert it to a float
    b = float(request.args.get('b'))  # Get the 'b' parameter from the URL query string, convert it to a float
    result = calc.add(a, b)  # Use the Calculator instance to add the two numbers
    return jsonify({'result': result})  # Return the result as a JSON response

# Define a route for subtraction operation
@app.route('/subtract', methods=['GET'])  # Specify the route for the subtraction operation and allow only GET requests
def subtract():
    a = float(request.args.get('a'))  # Get the 'a' parameter from the URL query string, convert it to a float
    b = float(request.args.get('b'))  # Get the 'b' parameter from the URL query string, convert it to a float
    result = calc.subtract(a, b)  # Use the Calculator instance to subtract the second number from the first
    return jsonify({'result': result})  # Return the result as a JSON response

# Define a route for multiplication operation
@app.route('/multiply', methods=['GET'])  # Specify the route for the multiplication operation and allow only GET requests
def multiply():
    a = float(request.args.get('a'))  # Get the 'a' parameter from the URL query string, convert it to a float
    b = float(request.args.get('b'))  # Get the 'b' parameter from the URL query string, convert it to a float
    result = calc.multiply(a, b)  # Use the Calculator instance to multiply the two numbers
    return jsonify({'result': result})  # Return the result as a JSON response

# Define a route for division operation
@app.route('/divide', methods=['GET'])  # Specify the route for the division operation and allow only GET requests
def divide():
    a = float(request.args.get('a'))  # Get the 'a' parameter from the URL query string, convert it to a float
    b = float(request.args.get('b'))  # Get the 'b' parameter from the URL query string, convert it to a float
    try:
        result = calc.divide(a, b)  # Use the Calculator instance to divide the first number by the second
    except ValueError as e:  # Catch the ValueError if division by zero is attempted
        return jsonify({'error': str(e)})  # Return an error message as a JSON response
    return jsonify({'result': result})  # Return the result as a JSON response

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode, allowing for easier debugging and hot reloading