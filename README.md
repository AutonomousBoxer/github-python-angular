# github-python-angular

## RESTful API Design

This project follows RESTful principles to design the backend, making it easier to understand and use. The following HTTP methods are used to perform CRUD operations:

- **GET**: Retrieve data from the server.
- **POST**: Send data to the server to create a new resource.
- **PUT**: Update an existing resource on the server.
- **DELETE**: Remove a resource from the server.

### Endpoints

Here are some examples of endpoints and their corresponding HTTP methods:

- **/users**
  - `GET /users`: Retrieve a list of users.
  - `POST /users`: Create a new user.
- **/users/<id>**
  - `GET /users/<id>`: Retrieve a specific user by ID.
  - `PUT /users/<id>`: Update a specific user by ID.
  - `DELETE /users/<id>`: Delete a specific user by ID.
- **/posts**
  - `GET /posts`: Retrieve a list of posts.
  - `POST /posts`: Create a new post.
- **/posts/<id>**
  - `GET /posts/<id>`: Retrieve a specific post by ID.
  - `PUT /posts/<id>`: Update a specific post by ID.
  - `DELETE /posts/<id>`: Delete a specific post by ID.

### Status Codes

The following status codes are used to indicate the result of each operation:

- **200 OK**: The request was successful.
- **201 Created**: The resource was successfully created.
- **204 No Content**: The resource was successfully deleted.
- **400 Bad Request**: The request was invalid or cannot be served.
- **404 Not Found**: The requested resource could not be found.
- **500 Internal Server Error**: An error occurred on the server.
