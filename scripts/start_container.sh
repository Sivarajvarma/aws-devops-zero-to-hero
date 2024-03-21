#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull sivarajvarma/simple-python-flask-app

# Run the Docker image as a container
docker run -d -p 5000:8000 sivarajvarma/simple-python-flask-app
