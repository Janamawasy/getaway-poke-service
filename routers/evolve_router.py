from fastapi import APIRouter, HTTPException
from connections.api_connector import ApiConnector

router = APIRouter()

@router.put('/')
async def evolve_poke(poke_name: str, trainer_name):
    try:
        connector = ApiConnector()
        res = connector.evolve(poke_name, trainer_name)
        return res
    except HTTPException as e:
        raise e