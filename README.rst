```
MusicCatalogue
==============

MusicCatalogue is a Django-based project for managing a music catalogue. It uses Django, Channels, and Daphne server for real-time functionality. The project includes production setup instructions, linting using Flake8, command automation with Makefile, Docker-compose for orchestration, Docker for containerization, and Poetry for package management.

API Documentation
-----------------

The MusicCatalogue project provides a RESTful API for managing users, albums, and artists. Below are the endpoints available in the API:

### Users

- `GET /api/users/`: Retrieve a list of users.
- `POST /api/users/`: Create a new user.
- `GET /api/users/{id}/`: Retrieve details of a specific user.
- `PUT /api/users/{id}/`: Update details of a specific user.
- `PATCH /api/users/{id}/`: Partially update details of a specific user.
- `DELETE /api/users/{id}/`: Delete a specific user.

### Albums

- `GET /api/albums/`: Retrieve a list of albums.
- `POST /api/albums/`: Create a new album.
- `GET /api/albums/{id}/`: Retrieve details of a specific album.
- `PUT /api/albums/{id}/`: Update details of a specific album.
- `PATCH /api/albums/{id}/`: Partially update details of a specific album.
- `DELETE /api/albums/{id}/`: Delete a specific album.

### Artists

- `GET /api/artists/`: Retrieve a list of artists.
- `POST /api/artists/`: Create a new artist.
- `GET /api/artists/{id}/`: Retrieve details of a specific artist.
- `PUT /api/artists/{id}/`: Update details of a specific artist.
- `PATCH /api/artists/{id}/`: Partially update details of a specific artist.
- `DELETE /api/artists/{id}/`: Delete a specific artist.

Schemas
-------

The MusicCatalogue API follows these schemas:

- **User**: Represents a user in the system.
- **Album**: Represents an album in the catalogue.
- **Artist**: Represents an artist in the catalogue.

Setup Instructions
------------------

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/MusicCatalogue.git
    ```

2. Install Poetry and Make for package management:
    - Prerequsite:
        Install Docker Compose.

    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    - Instructions to install make 
      https://www.geeksforgeeks.org/how-to-install-make-on-ubuntu/

3. Navigate to the project directory:

    ```bash
    cd MusicCatalogue
    ```

4. Install dependencies:

    ```bash
    make install
    - Override any setting you want inside local/settings.dev.py

    ```
5. Run Postgresql Db using Docker 
    ```bash
    make up-dependencies-only
    ```

6. Run migrations:

    ```bash
    make migrate
     ```

7. Run the development server:

    ```bash
    make run-server
    ```

8. Access the API at `http://localhost:8000/docs/`.

Linting and Testing
-------------------

Run Flake8 for linting:

```bash
poetry run flake8
```


Production Deployment
---------------------

For production deployment, the project can be containerized using Docker. Follow these steps:

1. Install Docker and Docker Compose.

2. Build the Docker image:

    ```bash
    docker-compose build
    ```

3. Run the containers:

    ```bash
    docker-compose up -d
    ```

4. Access the API at the specified URL.


```

