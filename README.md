# About The Project

I've created an API as described in the assignment,

I have used the FastAPI framework with MongoDB backend with Beanie ODM.

##### Choise of FastAPI and MongoDB
The combination of FastAPI and MongoDB is a great choice for building REST APIs due to their high performance, speed, flexibility, scalability, and ease of use.

Together, FastAPI and MongoDB are a great choice for building REST APIs that need to handle large amounts of unstructured data and traffic.

They provide a solid foundation for future development and can easily evolve and scale as your needs change over time.

##### Choise of Beanie ODM,

Beanie ODM provides a simple and intuitive API for querying and manipulating MongoDB data, supports type hinting, and offers automatic schema generation.

The ease of use and developer-friendly features make it a great choice for building Python applications that interact with MongoDB.

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


## Models

There are three main database models:

```User``` - A user model with name, user_name, password, role fields. Note: Roles are viewer, creator or admin.

```Post``` - A post model with title, content,creator_id fields.

```Like``` - A like model with doc_reference_id, liked_by, creation_date fields.


# Instructions

#### Starting the API
```bash
docker volume create mongo-volume
docker-compose build && docker-compose up -d
```
When finished visit http://localhost:8080/docs/ to interact with the API! \
better to register a User and the authenticate using /login route with your credentials, \
then using the token provided to authorize using SwaggerUI feature, by copying the token provided to the required field.

# Important notes

Required python version >=3.10+
