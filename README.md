# coride Flask CRUD API with MongoDB

This is a Flask application that provides a RESTful API for performing CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource.

## Features

- **Create** a new user
- **Read** all users or a single user by ID
- **Update** an existing user by ID
- **Delete** a user by ID

## Technologies Used

- **Flask**: A lightweight Python web framework
- **MongoDB**: NoSQL database for storing user data
- **Docker**: For containerizing the application
- **Flask-PyMongo**: Flask extension for interacting with MongoDB
- **Postman**: API testing tool

## API Endpoints

| Method | Endpoint          | Description                          |
|--------|-------------------|--------------------------------------|
| GET    | `/users`          | Retrieve a list of all users         |
| GET    | `/users/<id>`     | Retrieve a single user by ID         |
| POST   | `/users`          | Create a new user                    |
| PUT    | `/users/<id>`     | Update an existing user by ID        |
| DELETE | `/users/<id>`     | Delete a user by ID                  |

## Requirements

- Python 3.8+
- Flask
- MongoDB
- Docker

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MOHDZAMA/coride.git
cd coride
