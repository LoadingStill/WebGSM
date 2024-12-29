# Base image
FROM python:3.9.21-bookworm

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Make sure .env will work
RUN pip install python-dotenv


# Expose port and run Flask
EXPOSE 5000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
