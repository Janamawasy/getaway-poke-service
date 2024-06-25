from fastapi import APIRouter, HTTPException
from api_connector import ApiConnector

router = APIRouter()

@router.post('/')
async def create_trainer(trainer_name: str, trainer_town: str):
    try:
        connector = ApiConnector()
        res = connector.create_trainer(trainer_name, trainer_town)
        return res
    except HTTPException as e:
        raise e

@router.delete('/')
async def delete_trainer(trainer_name: str):
    try:
        connector = ApiConnector()
        res = connector.delete_trainer(trainer_name)
        return res
    except HTTPException as e:
        raise e

@router.post('/pokemons/')
async def add_pokemon_to_trainer(pokemon_name: str, trainer_name: str):
    try:
        connector = ApiConnector()
        res = connector.add_pokemon_to_trainer(pokemon_name, trainer_name)
        return res
    except HTTPException as e:
        raise e

@router.put('/pokemons/')
async def delete_pokemon_of_trainer(pokemon_name, trainer_name):
    try:
        connector = ApiConnector()
        res = connector.delete_pokemon_from_trainer(pokemon_name, trainer_name)
        return res
    except HTTPException as e:
        raise e

