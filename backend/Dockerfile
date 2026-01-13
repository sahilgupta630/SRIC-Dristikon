# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (needed for some python packages like faiss maybe, but usually slim is fine for faiss-cpu)
# If we need build tools:
# RUN apt-get update && apt-get install -y build-essential

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any exact dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# Default command (will be overridden in docker-compose)
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
