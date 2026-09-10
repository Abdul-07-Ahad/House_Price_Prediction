# Base image
FROM python:3.12-slim

# Working directory inside the container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Flask uses port 5000
EXPOSE 5000

# Command to start the application
CMD ["python", "app.py"]
