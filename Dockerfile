# Base image
FROM python:3.9-slim

# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app
COPY * .

# Expose Flask port
EXPOSE 8082


# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask server
CMD ["flask", "run", "--host=0.0.0.0", "--port=8082"]
