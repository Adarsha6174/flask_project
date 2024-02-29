# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the Flask application code into the container
COPY . /app/

# Expose the port that the Flask app will run on
EXPOSE 5000

# Start the Flask application
CMD ["python", "new.py"]

