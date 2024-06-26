import os
import requests
from fastapi import HTTPException
from requests import RequestException
from dotenv import load_dotenv
from fastapi.responses import StreamingResponse
import io

load_dotenv()


class ApiImageGenerator:
    def __init__(self):
        self.image_generator_service = os.getenv('SERVICE3_URL')

    def generate_battle_image(self, poke1_name, poke2_name):
        try:
            response = requests.post(
                f"{self.image_generator_service}/battle?poke1_name={poke1_name}&poke2_name={poke2_name}")
            response.raise_for_status()
            return StreamingResponse(io.BytesIO(response.content), media_type="image/svg+xml")
        except RequestException as e:
            raise HTTPException(status_code=400, detail=str(e))

    def generate_evolution_image(self, poke1_name, poke2_name):
        try:
            response = requests.post(
                f"{self.image_generator_service}/evolve?poke1_name={poke1_name}&poke2_name={poke2_name}")
            response.raise_for_status()
            return StreamingResponse(io.BytesIO(response.content), media_type="image/svg+xml")
        except RequestException as e:
            raise HTTPException(status_code=400, detail=str(e))

    def generate_image(self, prompt):
        try:
            response = requests.post(f"{self.image_generator_service}/?prompt={prompt}")
            response.raise_for_status()
            return StreamingResponse(io.BytesIO(response.content), media_type="image/svg+xml")
        except RequestException as e:
            raise HTTPException(status_code=400, detail=str(e))

    def testing_image(self):
        try:
            response = requests.post(f"{self.image_generator_service}/test")
            response.raise_for_status()
            return StreamingResponse(io.BytesIO(response.content), media_type="image/png")
        except RequestException as e:
            raise HTTPException(status_code=400, detail=str(e))
