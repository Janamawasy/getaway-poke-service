# Pokemon-Project

This service is a gateway for a microservice architecture project. It serves as a single access point and acts as a proxy for multiple services. A service gateway enables transformations, routing, and common processing across all the services. This project uses a FastAPI server to interact with and manage requests to:

service 1: pokemon service - interact with Pokemon API and MySQL

service 2: image service - interact with Pokemon API and Mongo DB

service 3: image generator service - interact with an AI API

## Services Features

  ### [poke service](LINK_TO_GATEWAY_PROJECT).
  
  - Search Pokemon by id or name
  - Search all Pokemons by trainer or type
  - Search all trainers of a specific Pokemon
  - Add new Pokemon using external API
  - Add new trainer
  - Add Pokemon to trainer
  - Delete Pokemon or trainer
  - Delete Pokemon from trainer
  - Evolve Pokemon of specific trainer

  ### [poke images service](LINK_TO_GATEWAY_PROJECT).
  
  - Retrieve a Pokemon image by Pokemon name
  - Add a new Pokemon image
  - Delete an existing Pokemon image
  - Update an existing Pokemon image
  - Display a Pokemon image

  ### [image generator service](LINK_TO_GATEWAY_PROJECT).
    
  - 




## env Setup

  ```
  SERVICE1_URL=http://127.0.0.1:8001
  SERVICE2_URL=http://127.0.0.1:8002
  SERVICE3_URL=http://127.0.0.1:8003
  ```


## Testing

run the tests:

    ```
      tests/proj_tests.py
    ```
