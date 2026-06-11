# 📘 Assignment: Containerize and Deploy a FastAPI App with Docker

## 🎯 Objective

Containerize a FastAPI application using Docker, run it locally, and add a basic GitHub Actions workflow that builds the image. Students will learn Dockerfiles, image builds, and simple CI integration.

## 📝 Tasks

### 🛠️ Create and Containerize a FastAPI App

#### Description

Start from the provided FastAPI starter app, write a `Dockerfile` to build a production-ready image, and run the container locally. Then add a GitHub Actions workflow that builds the Docker image (optionally pushes it to a registry using secrets).

#### Requirements

Completed assignment should:

- Include a working `Dockerfile` that installs dependencies and runs the FastAPI app with `uvicorn`.
- Be able to build the image locally with `docker build -t fastapi-deploy .` and run it with `docker run -p 8000:8000 fastapi-deploy`.
- Include `requirements.txt` for Python dependencies.
- Provide a sample GitHub Actions workflow in `.github/workflows/docker-build.yml` that builds the Docker image and (optionally) pushes to Docker Hub when secrets are configured.
- Document the local build and run steps in the README and include example `docker` and `curl` commands.


## Example local commands

```bash
# Build the Docker image
docker build -t fastapi-deploy .

# Run the container
docker run --rm -p 8000:8000 fastapi-deploy

# Test the API
curl http://localhost:8000/items
```

## Starter files included

- `main.py` - Minimal FastAPI app.
- `Dockerfile` - Container build instructions.
- `requirements.txt` - Dependencies.
- `.github/workflows/docker-build.yml` - Example CI workflow to build the image.

## Submission notes

- Verify the image builds and the container serves the API on port 8000.
- Optional: configure Docker Hub secrets and confirm the workflow pushes an image.
