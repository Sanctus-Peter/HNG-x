# HNG X-2
## Backend Track - Task 2

This is a simple REST API for performing CRUD (Create, Read, Update, Delete) operations on a "person" resource. It allows you to add, retrieve, update, and delete person records in a database. The API is designed to be flexible and secure, with dynamic parameter handling and validation.

## Features

### CRUD Operations

- **CREATE**: Add a new person to the database.
  - Endpoint: `/api`
  - Method: POST
  - Request Body: JSON data containing person details (e.g., name, age, address)
  - Response: JSON response with the newly created person's details.

- **READ**: Fetch details of a person by user ID.
  - Endpoint: `/api/{user_id}`
  - Method: GET
  - Response: JSON response with the person's details.

- **UPDATE**: Modify details of an existing person.
  - Endpoint: `/api/{user_id}`
  - Method: PUT
  - Request Body: JSON data containing updated person details
  - Response: JSON response with the updated person's details.

- **DELETE**: Remove a person.
  - Endpoint: `/api/{user_id}`
  - Method: DELETE
  - Response: JSON response indicating the deletion status.

## Dependencies
- FastAPI
    - fastapi
    - uvicorn
    - pydantic
  
- django
    - django
    - djangorestframework


## Framework Used
- [FastAPI](fastapi_app)
- [django](django)