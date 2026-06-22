from fastapi import FastAPI, APIRouter
from database.database import engine, Base

# OBS: Você precisa importar a Model para o SQLAlchemy "enxergar" a classe, No Spring era so inicar servidor
from models.pet_model import PetModel

# Agora sim, quando ele rodar esta linha, ele já sabe que a classe PetModel existe
Base.metadata.create_all(bind=engine)

app = FastAPI()
router = APIRouter()

@router.get('/')
def first():
    return 'Ola mundo, Hello world'

app.include_router(router)