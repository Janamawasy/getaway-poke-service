from fastapi import APIRouter, HTTPException
from connections.api_connector import ApiConnector

router = APIRouter()

@router.get('/')
async def get_image(poke_name: str):
    try:
        connector = ApiConnector()
        res = connector.get_image(poke_name)
        return res
    except HTTPException as e:
        raise e


@router.post('/')
async def add_image(poke_name):
    try:
        connector = ApiConnector()
        res = connector.add_image(poke_name)
        return res
    except HTTPException as e:
        raise e


@router.put('/')
async def update_image(poke_name, new_image_url):
    try:
        connector = ApiConnector()
        res = connector.update_image(poke_name, new_image_url)
        return res
    except HTTPException as e:
        raise e
