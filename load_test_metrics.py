import time
import psutil
from SampleCalc import Calculator  # Assuming SampleCalc.py contains the Calculator class


# Function to monitor system resources (CPU and memory usage)
def monitor_resources():
    # Get CPU and memory usage
    cpu_usage = psutil.cpu_percent(interval=1)  # Measure CPU usage percentage over a 1-second interval
    memory = psutil.virtual_memory()  # Get memory usage statistics
    memory_usage = memory.percent  # Get the percentage of used memory

    # Print system stats to track resource usage
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")


# Function to perform a load test on the Calculator class
def load_test():
    calc = Calculator()  # Create an instance of the Calculator class
    start_time = time.time()  # Record the start time of the load test

    try:
        # Loop to simulate a high load on the calculator
        for i in range(1000000):  # Run a loop one million times to simulate load
            calc.add(10, 5)  # Perform an addition operation
            calc.multiply(5, 4)  # Perform a multiplication operation

            # Monitor resources every 10000 iterations to avoid overwhelming output
            if i % 10000 == 0:
                monitor_resources()  # Call the function to print CPU and memory usage

    except Exception as e:
        # Handle any exceptions that occur during the load test
        print(f"Error occurred during load test: {e}")

    end_time = time.time()  # Record the end time of the load test
    # Calculate and print the total time taken for the load test
    print(f"Load Test Completed in {end_time - start_time} seconds")


# Main function to execute the load test
if __name__ == "__main__":
    load_test()  # Call the load test function
