# Dockerfile to build a container image for the app
# Based on the official Python 3.10 slim image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install apt-get install wkhtmltopdf

RUN apt-get update && apt-get install -y wkhtmltopdf

# Install and configure poetry
RUN pip install poetry
RUN poetry config virtualenvs.create false

# Install any needed packages specified in pyproject.toml
RUN poetry install

# Make port 8000 available to the world outside this container
EXPOSE 8000

