# Pokemon-Project

This service is a gateway for a microservice architecture project. It serves as a single access point and acts as a proxy for multiple services. A service gateway enables transformations, routing, and common processing across all the services. This project uses a FastAPI server to interact with and manage requests to:

service 1: pokemon service - interact with Pokemon API and MySQL

service 2: image service - interact with Pokemon API and Mongo DB

service 3: image generator service - interact with an AI API

## Services Features

  ### [poke service](https://github.com/Janamawasy/pokemon_service/tree/main).
  
  - Search Pokemon by id or name
  - Search all Pokemons by trainer or type
  - Search all trainers of a specific Pokemon
  - Add new Pokemon using external API
  - Add new trainer
  - Add Pokemon to trainer
  - Delete Pokemon or trainer
  - Delete Pokemon from trainer
  - Evolve Pokemon of specific trainer

  ### [poke images service](https://github.com/Janamawasy/poke_images_service).
  
  - Retrieve a Pokemon image by Pokemon name
  - Add a new Pokemon image
  - Delete an existing Pokemon image
  - Update an existing Pokemon image
  - Display a Pokemon image

  ### [image generator service](https://github.com/Janamawasy/generate-images-service).
    
  - Generate an image based on a provided prompt.
  - Generate an imaginary fusion image between two Pokémon.
  - Generate a hypothetical evolution image for Pokémon.

## Getaway Endpoints
![Description of the image](/getaway_endpoint.png)


## Endpoints diagram
![Description of the image](/endpoints_diagram.png)

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
