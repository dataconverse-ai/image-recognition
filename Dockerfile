# Use the official Python 3.11 image from the Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy the pyproject.toml and poetry.lock files (assuming you are using Poetry)
COPY pyproject.toml poetry.lock* /app/

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of your application's code
COPY . /app

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the application:
CMD ["uvicorn", "src.image_recognition.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
