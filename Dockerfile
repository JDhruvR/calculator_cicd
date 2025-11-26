# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Run the tests to ensure the code is working.
# If tests fail, the docker build will fail, which is a good check.
RUN python -m unittest test_calculator.py

# Define the command to run your application
CMD ["python", "calculator.py"]
