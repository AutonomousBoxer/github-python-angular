# github-python-angular

## RESTful API Design

This project follows RESTful principles to design the backend, making it easier to understand and use. The following HTTP methods are used to perform CRUD operations:

- **GET**: Retrieve data from the server.
- **POST**: Send data to the server to create a new resource.
- **PUT**: Update an existing resource on the server.
- **DELETE**: Remove a resource from the server.

## Setting up and running the backend

1. Create a virtual environment:
   ```sh
   python -m venv venv
   ```

2. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```sh
     source venv/bin/activate
     ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the Flask application:
   ```sh
   flask run
   ```

5. The backend will be available at `http://localhost:5000`.

## Endpoints

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

## Status Codes

The following status codes are used to indicate the result of each operation:

- **200 OK**: The request was successful.
- **201 Created**: The resource was successfully created.
- **204 No Content**: The resource was successfully deleted.
- **400 Bad Request**: The request was invalid or cannot be served.
- **404 Not Found**: The requested resource could not be found.
- **500 Internal Server Error**: An error occurred on the server.

## Setting up and running the Angular frontend

1. Navigate to the `frontend` directory:
   ```sh
   cd frontend
   ```

2. Install the dependencies:
   ```sh
   npm install
   ```

3. Start the Angular development server:
   ```sh
   ng serve
   ```

4. Open your browser and navigate to `http://localhost:4200` to see the Angular frontend in action.
