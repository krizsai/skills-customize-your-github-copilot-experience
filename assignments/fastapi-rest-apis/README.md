# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build a simple RESTful API using the FastAPI framework, including request/response models, endpoint routing, and basic CRUD operations.

## 📝 Tasks

### 🛠️ Implement a REST API for a simple resource

#### Description

Create a FastAPI application that exposes CRUD endpoints for a resource called `Item`. Implement request validation with Pydantic models and use an in-memory store (list or dict) for persistence during runtime.

#### Requirements

Completed assignment should:

- Use `FastAPI` and `Pydantic` for the application and models.
- Provide endpoints: `GET /items` (list), `GET /items/{id}` (retrieve), `POST /items` (create), `PUT /items/{id}` (update), `DELETE /items/{id}` (delete).
- Validate request bodies with Pydantic models and return appropriate HTTP status codes.
- Use async endpoint handlers where appropriate.
- Include example `curl` commands showing how to call each endpoint.
- Include a minimal `requirements.txt` listing the dependencies.


## Example `curl` commands

```bash
# Create an item
curl -X POST http://localhost:8000/items -H "Content-Type: application/json" -d '{"name":"Widget","price":9.99}'

# List items
curl http://localhost:8000/items

# Get single item
curl http://localhost:8000/items/1

# Update item
curl -X PUT http://localhost:8000/items/1 -H "Content-Type: application/json" -d '{"name":"Updated","price":12.5}'

# Delete item
curl -X DELETE http://localhost:8000/items/1
```


## Starter files

- `main.py` - Minimal FastAPI app with in-memory store.
- `requirements.txt` - Package list to run the app.


## Submission notes

- Run the app with `uvicorn main:app --reload` and verify endpoints work.
- You may extend the app with persistence (SQLite) for extra credit.
