# HNG X-2

## Backend Track - Task 2

This is a simple REST API for performing CRUD (Create, Read, Update, Delete) operations on a "person" resource. It allows you to add, retrieve, update, and delete person records in a database. The API is designed to be flexible and secure, with dynamic parameter handling and validation.

## Programming Language and Database

- Programming Language: Python
- Web Framework:
  - [FastAPI](fastapi_app)
  - [django](django)
- Database: PostgreSQL

## Dependencies

- FastAPI
  - fastapi
  - uvicorn
  - pydantic
  - psycopg2-binary
  - python-dotenv
  - sqlalchemy
- django
  - django
  - djangorestframework

## Documentation

[api doc](https://hng-task-2-gcrn.onrender.com/docs)

## Implementation

1. Initialize a new FastAPI project and set up the necessary routes for CRUD operations.
2. Create functions for each CRUD operation: Create, Read, Update, and Delete.
3. Implement secure database interactions to prevent SQL injections using PostgreSQL as the database.

## Setup Instructions

1. Clone this repository.
2. Install project dependencies using `pip install -r requirements.txt`.
3. Set up a PostgreSQL database and update the database connection settings in `config.py`.
4. Run the FastAPI application using `uvicorn main:app --reload`.

## API Usage

- ### Create a Person (POST /api)

  Request:

  ```json
  POST /api
  {
    "name": "John Doe",
  }
  ```

  Response:

  ```json
  {
    "id": 669f59a0-c2e6-4c12-8cea-ef1bbab75da2,
    "name": "John Doe"
  }
  ```

- ### Read a Person (GET /api/{id})

  Request:

  ```json
  GET /api/669f59a0-c2e6-4c12-8cea-ef1bbab75da2
  ```

  Response:

  ```json
  {
    "id": 669f59a0-c2e6-4c12-8cea-ef1bbab75da2,
    "name": "John Doe"
  }
  ```

- ### Update a Person (PUT /api/{id})

  Request:

  ```json
  PUT /api/669f59a0-c2e6-4c12-8cea-ef1bbab75da2
  {
    "name": "John Jane Doe",
  }
  ```

  Response:

  ```json
  {
    "id": 669f59a0-c2e6-4c12-8cea-ef1bbab75da2,
    "name": "John Jane Doe"
  }
  ```

- ### Delete a Person (DELETE /api/{id})

  Request:

  ```json
  DELETE /api/669f59a0-c2e6-4c12-8cea-ef1bbab75da2
  ```

  Response:

  ```json

  ```
