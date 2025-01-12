# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY static/ /app/static/         # Copy the static folder
COPY templates/ /app/templates/   # Copy the templates folder
COPY app.py /app/app.py           # Copy the Flask app

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
