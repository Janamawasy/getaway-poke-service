from fastapi import APIRouter, HTTPException
from connections.image_gen_api_connector import ApiImageGenerator

router = APIRouter()

@router.post('/battle')
async def generate_battle(poke1_name: str, poke2_name: str):
    try:
        connector = ApiImageGenerator()
        res = connector.generate_battle_image(poke1_name, poke2_name)
        return res
    except HTTPException as e:
        raise e


@router.post('/evolve')
async def generate_evolution(poke1_name: str, poke2_name: str):
    try:
        connector = ApiImageGenerator()
        res = connector.generate_evolution_image(poke1_name, poke2_name)
        return res
    except HTTPException as e:
        raise e


@router.post('/')
async def generate_image(prompt: str):
    try:
        connector = ApiImageGenerator()
        res = connector.generate_image(prompt)
        return res
    except HTTPException as e:
        raise e

@router.post('/test')
async def generate_image():
    try:
        connector = ApiImageGenerator()
        res = connector.testing_image()
        return res
    except HTTPException as e:
        raise e
