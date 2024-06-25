import requests
import os
from dotenv import load_dotenv

load_dotenv()

poke_train_service = os.getenv("SERVICE1_URL")
poke_images_service = os.getenv("SERVICE2_URL")


def compensate_add_pokemon(poke_name, status_code_service1, status_code_service2):
    if status_code_service1 == 200:
        # service 1 succeed and service 2 failed => rollback service1
        requests.delete(f"{poke_train_service}/pokemons/?pokemon_name={poke_name}")

    if status_code_service2 == 200:
        # service 1 succeed and service 2 failed => rollback service1
        requests.delete(f"{poke_images_service}/?poke_name={poke_name}")

