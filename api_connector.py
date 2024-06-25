import os
import requests
from fastapi import HTTPException
from requests import RequestException
from utils.compensate_utils import compensate_add_pokemon
from dotenv import load_dotenv
from fastapi.responses import StreamingResponse
import io

load_dotenv()

class ApiConnector:
    def __init__(self):
        self.poke_trainer_service = os.getenv('SERVICE1_URL')
        self.poke_images_service = os.getenv('SERVICE2_URL')

    def add_pokemon(self, poke_name):
        response1 = None
        response2 = None
        try:
            print('in add poke!!!')
            response1 = requests.post(f"{self.poke_trainer_service}/pokemons/?pokemon_name={poke_name}")
            print(response1.status_code)
            response2 = requests.post(f"{self.poke_images_service}/?poke_name={poke_name}")
            print(response2.status_code)

            print(response1, response2)
            # Raises an error for 4xx/5xx responses
            response1.raise_for_status()
            response2.raise_for_status()
            return {"details": "pokemon added successfully"}

        except RequestException as e:
            status_code_service1 = response1.status_code
            status_code_service2 = response2.status_code

            # handle failed calls:
            compensate_add_pokemon(poke_name, status_code_service1, status_code_service2)

            if status_code_service1 == 409 or status_code_service1 == 404:
                return response1.json()
            if status_code_service2 == 409 or status_code_service2 == 404:
                return response2.json()
            raise HTTPException(status_code=400, detail={"detail": "An error occurred", "error": str(e)})

    def get_pokemon_data(self, poke_name):
        pokemon_info = "Failed to retrieve pokemon data"
        pokemon_image = "Failed to retrieve pokemon image"
        try:
            response1 = requests.get(f"{self.poke_trainer_service}/pokemons/by-name/?pokemon_name={poke_name}")
            pokemon_info = response1.json()
            print('pokemon_info', pokemon_info)
            response1.raise_for_status()
        except RequestException as e:
            print(f"Failed to retrieve Pokémon info: {e}")

        try:
            response2 = requests.get(f"{self.poke_images_service}/data/?poke_name={poke_name}")
            response2.raise_for_status()
            pokemon_image = response2.json()
        except RequestException as e:
            print(f"Failed to retrieve Pokémon image: {e}")

        return {
            'pokemon_info': pokemon_info,
            'pokemon_image': pokemon_image
        }

    def get_pokemon_by_trainer(self, trainer_name):
        try:
            response1 = requests.get(f"{self.poke_trainer_service}/pokemons/by-trainer/?trainer_name={trainer_name}")
            pokemons_res = response1.json()
            response1.raise_for_status()
            return {"pokemons": pokemons_res}
        except RequestException as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_pokemon_by_type(self, type_name):
        try:
            response1 = requests.get(f"{self.poke_trainer_service}/pokemons/by-type/?pokemon_type={type_name}")
            pokemons = response1.json()
            response1.raise_for_status()
            return {"pokemons": pokemons}
        except RequestException as e:
            raise HTTPException(status_code=400, detail=str(e))

    def add_pokemon_to_trainer(self, poke_name, trainer_name):
        response1 = None
        try:
            response1 = requests.post(
                f"{self.poke_trainer_service}/trainers/pokemon/?pokemon_name={poke_name}&trainer_name={trainer_name}")
            response1.raise_for_status()
            return {"detail": "pokemon was successfully added to the trainer"}
        except RequestException as e:
            if response1.status_code == 409:
                raise HTTPException(status_code=409, detail={'detail': f'{trainer_name} already is training {poke_name} pokemon', 'error': str(e)})
            if response1.status_code == 404:
                raise HTTPException(status_code=404, detail={'detail': f'{trainer_name} or {poke_name} are not exist, double check pokemon and trainer names', 'error': str(e)})
            else:
                raise HTTPException(status_code=400, detail=str(e))

    def delete_pokemon_from_trainer(self, poke_name, trainer_name):
        res = None
        try:
            response1 = requests.put(
                f"{self.poke_trainer_service}/trainers/?pokemon_name={poke_name}&trainer_name={trainer_name}")

            res = response1.json()
            print(res)
            response1.raise_for_status()
            return {"detail": "Pokémon was successfully deleted to the trainer"}

        except RequestException as e:
            raise HTTPException(status_code=400, detail=res['detail'])

    def evolve(self, poke_name, trainer_name):
        response1 = None
        response2 = None
        evolved_pokemon = None
        json_response1 = None
        json_response2 = None

        try:
            response1 = requests.put(
                f"{self.poke_trainer_service}/evolve/?pokemon_name={poke_name}&trainer_name={trainer_name}")
            json_response1 = response1.json()

            response1.raise_for_status()

            if isinstance(json_response1, str):
                raise HTTPException(status_code=400, detail=json_response1)

            evolved_pokemon = json_response1.get('evolved_pokemon')

            response2 = requests.post(f"{self.poke_images_service}/?poke_name={evolved_pokemon}")
            json_response2 = response2.json()

            response2.raise_for_status()

            return {"detail": "evolved successfully"}

        except RequestException as e:
            if response1.status_code != 200:
                raise HTTPException(status_code=400, detail=json_response1['detail'])
                # print(f"Error in evolve {poke_name}: {e}")
            if response2.status_code != 200:
                raise HTTPException(status_code=400, detail=json_response2['detail'])
            else:
                raise HTTPException(status_code=400, detail=str(e))

    def get_image(self, poke_name):
        json_response = None
        try:
            response2 = requests.get(f"{self.poke_images_service}/image/?poke_name={poke_name}")
            response2.raise_for_status()
            return StreamingResponse(io.BytesIO(response2.content), media_type="image/svg+xml")
        except RequestException as e:
            raise HTTPException(status_code=400, detail=json_response['detail'] if json_response else str(e))

    def add_image(self, poke_name):
        json_response = None
        try:
            response2 = requests.post(f"{self.poke_images_service}/?poke_name={poke_name}")
            json_response = response2.json()
            response2.raise_for_status()
            return {"detail": "image added successfully"}
        except RequestException as e:
            raise HTTPException(status_code=400, detail=json_response['detail'])

    def update_image(self, poke_name, new_image_url):
        json_response = None
        try:
            response2 = requests.put(f"{self.poke_images_service}/?poke_name={poke_name}&new_image_url={new_image_url}")
            json_response = response2.json()
            response2.raise_for_status()
            return {"detail": "image replaced successfully"}
        except RequestException as e:
            raise HTTPException(status_code=400, detail=json_response['detail'])

    def create_trainer(self, trainer_name, town):
        json_response = None
        try:
            response2 = requests.post(
                f"{self.poke_trainer_service}/trainers/trainer/?trainer_name={trainer_name}&trainer_town={town}")
            json_response = response2.json()
            response2.raise_for_status()
            return {"detail": "trainer created successfully"}
        except RequestException as e:
            raise HTTPException(status_code=400, detail=json_response['detail'])

    def delete_trainer(self, trainer_name):
        json_response = None
        try:
            response2 = requests.delete(f"{self.poke_trainer_service}/trainers/?trainer_name={trainer_name}")
            json_response = response2.json()
            response2.raise_for_status()
            return {"detail": "trainer deleted successfully"}
        except RequestException as e:
            raise HTTPException(status_code=400, detail=json_response['detail'])
