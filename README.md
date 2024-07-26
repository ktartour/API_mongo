# Project NoSQL & PYTHON

## Project description

The goal of the project is to program an Python API using FastAPI swagger.
By using this API one would be able to perform CRUD operations on a MongoDB database. 

## Main functions

* Get a list of teachers

* Get a list of students with corresponding class

* Get a list of students within a given class

* Get a student marks

* Get students marks regarding a teacher

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
