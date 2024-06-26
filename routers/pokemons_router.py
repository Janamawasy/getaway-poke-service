from fastapi import APIRouter, HTTPException
from connections.api_connector import ApiConnector

router = APIRouter()


@router.get('/')
async def get_pokemon_data(poke_name: str):
    try:
        connector = ApiConnector()
        res = connector.get_pokemon_data(poke_name)
        return res
    except HTTPException as e:
        raise e

@router.get('/by-type/')
async def get_pokemons_by_type(pokemon_type: str):
    try:
        connector = ApiConnector()
        res = connector.get_pokemon_by_type(pokemon_type)
        return res
    except HTTPException as e:
        raise e


@router.get('/by-trainer/')
async def get_pokemons_by_trainer(trainer_name: str):
    try:
        connector = ApiConnector()
        res = connector.get_pokemon_by_trainer(trainer_name)
        return res
    except HTTPException as e:
        raise e


@router.post('/')
async def add_new_pokemon(pokemon_name: str):
    try:
        connector = ApiConnector()
        res = connector.add_pokemon(pokemon_name)
        return res
    except HTTPException as e:
        raise e




