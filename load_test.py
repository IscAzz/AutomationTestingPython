from locust import HttpUser, task, between  # Import necessary classes from Locust to create load tests

class CalculatorUser(HttpUser):  # Define a user class that simulates behavior for load testing
    wait_time = between(1, 2)  # Simulate a wait time of 1 to 2 seconds between each task to mimic real user behavior

    @task  # Mark this method as a task that Locust will execute during the load test
    def test_add(self):
        self.client.get("/add?a=5&b=3")  # Make a GET request to the /add endpoint with parameters a=5 and b=3

    @task  # Mark this method as a task that Locust will execute during the load test
    def test_subtract(self):
        self.client.get("/subtract?a=10&b=5")  # Make a GET request to the /subtract endpoint with parameters a=10 and b=5

    @task  # Mark this method as a task that Locust will execute during the load test
    def test_multiply(self):
        self.client.get("/multiply?a=6&b=7")  # Make a GET request to the /multiply endpoint with parameters a=6 and b=7

    @task  # Mark this method as a task that Locust will execute during the load test
    def test_divide(self):
        self.client.get("/divide?a=20&b=4")  # Make a GET request to the /divide endpoint with parameters a=20 and b=4
