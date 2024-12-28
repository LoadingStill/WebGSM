# Base image
FROM python:3.9-slim

# Install dependencies
WORKDIR /app
COPY app/backend/requirements.txt .
RUN pip install -r requirements.txt

# Copy app
COPY app .

# Expose Flask port
EXPOSE 8082

# Run the server
CMD ["python", "backend/server.py"]
