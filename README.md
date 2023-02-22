# About The Project

I've created an API as described in the assignment,

I have used the FastAPI framework with MongoDB backend with Beanie ODM.

Choosing MongoDB as the backend is simply because of comfort and ease, this API can be created with any database \
There are no significant changes, just the ease of development.

I have created 4 main tag routes according to REST architecture.

### Authentication

``` POST /login``` - To log in using username and password to acquire the JWT access token

### Users

```GET /api/v1/users/``` - To get all registered users

```POST /api/v1/users/``` - To register a new user

```GET /api/v1/users/{id}``` - To get one user by its id in the DB

```GET /api/v1/users/me``` - To get the current active logged in user

### Posts (Protected routes)

```GET /api/v1/posts/``` - To get all posts

```POST /api/v1/posts/``` - To add a new post

```GET /api/v1/posts/{id}``` - To get one post by its id in the DB

```PUT /api/v1/posts/{id}``` - To update a post by its id in the DB

```DELETE /api/v1/posts/{id}``` - To delete a post by its id in the DB

### Likes (Protected routes)

```GET /api/v1/likes/{post_id}``` - To get liked post by its id in the DB

```POST /api/v1/likes/{post_id}``` - To add a new like to a post by its id in the DB

```DELETE /api/v1/likes/{post_id}``` - To delete a like to a post by its post id in the DB

Choosing FastAPI because of its simplicity and its nice OpenAPI and Swagger UI allows exploring in more depth about this API

Just visit http://localhost:8080/docs/

# Instruction to run

## Initalize enviorment 

```bash
python3 -m venv venv
source ./venv/bin/activate
python -m pip install -r requirments.txt
```

## Running Database

```bash
docker volume create mongo-volume
docker-compose up -d
```

## Starting the API

```bash
python ./backend/main.py
```

# Important notes

Required python version >=3.10+
