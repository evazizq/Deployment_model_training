# Use an official Python image
FROM python:3.13-slim

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy only the dependency files first to leverage Docker caching
COPY pyproject.toml poetry.lock /app/

# Install dependencies without creating a virtual environment
RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the project files
COPY . /app/

# Copy the data directory
COPY data /app/data

# Command to run the inference script
CMD ["poetry", "run", "python", "src/main.py"]