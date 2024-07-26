# Project NoSQL & PYTHON

## Project description

The goal of the project is to program an Python API using FastAPI swagger.
By using this API one would be able to perform CRUD operations on a MongoDB database as well as common requests

## Project architecture
```
API_mongo/
|-- README.md
|-- requirements.txt
|-- docker-composte.yml
|-- .gitignore
|-- Dockerfile
|-- src/
|       |-- main.py
|       |-- routes/
|       |       |-- CRUD_eleve_route.py
|       |       |-- CRUD_note_route.py
|       |       |-- question_projet_route.py
|       | 
|       |-- config/
|       |       |-- db.py
|       |       |-- ...
|       | 
|       |-- services/
|       |       |-- CRUD_eleve_service.py
|       |       |-- CRUD_note_service.py
|       |       |-- question_projet_service.py
|       | 
|       |-- schemas/
|               |-- note_schema.py
|-- data/
|       |-- CSV_from_SQL_to_MongoDB.zip
```

## Main functions

* Get a list of teachers
* Get a list of students with corresponding class
* Get a list of students within a given class
* Get a student marks
* Get students marks regarding a teacher
* Create, Read, Update, Delete a note or a student

## Run

* Install the dependencies

  ``` bash
  pip install -r requirements.txt
  ```

* Launch the project

  ``` bash
  fastapi dev main.py
  ```

  Go to [localhost:8000](http://127.0.0.1:8000/) for the app  
  Or [localhost:8000/docs](http://127.0.0.1:8000/docs) for the documentation

## Run with docker

As an alternative, you can launch the project with docker:

* Create the image

  ``` bash
  docker-compose build
  ```

* Run the container

  ``` bash
  docker-compose run
  ```

  Go to [localhost:8000](http://127.0.0.1:8000/)
