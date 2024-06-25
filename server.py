import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from routers import evolve_router, trainers_router, pokemons_router, image_router

load_dotenv()

host = os.getenv('SERVER_HOST')
port = os.getenv('SERVER_PORT')

app = FastAPI()

app.include_router(pokemons_router.router, prefix='/pokemons')
app.include_router(trainers_router.router, prefix='/trainers')
app.include_router(image_router.router, prefix='/images')
app.include_router(evolve_router.router, prefix='/evolve')


@app.get('/')
def root():
    return f'Lost? The magic happens at {host}:{port}/docs. Don\'t miss out!'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

