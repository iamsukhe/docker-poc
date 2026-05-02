# Use the official Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port Flask/Gunicorn will run on
EXPOSE 8080

# Run the web service using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]