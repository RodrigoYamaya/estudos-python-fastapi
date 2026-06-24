from fastapi import FastAPI
from database.database import engine, Base

# OBS: Você precisa importar a Model para o SQLAlchemy "enxergar" a classe, No Spring era so inicar servidor
from models.pet_model import PetModel
from routes import pet_routes

# Agora sim, quando ele rodar esta linha, ele já sabe que a classe PetModel existe
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(pet_routes.router)
