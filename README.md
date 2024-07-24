# API_mongo

## Run

* Install the dependencies

  ``` bash
  pip install -r requirements.txt
  ```

* Launch the project

  ``` bash
  fastapi dev main.py
  ```

  Go to localhost:8000 for the app  
  Or localhost:8000/docs for the documentation

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

  Go to localhost:8000