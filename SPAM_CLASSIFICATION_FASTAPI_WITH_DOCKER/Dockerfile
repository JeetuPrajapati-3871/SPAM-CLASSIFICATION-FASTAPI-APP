# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Installing dependencies
RUN pip install -r requirements.txt

# Copy app files
COPY . /app

# Expose port FastAPI will run on
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]
