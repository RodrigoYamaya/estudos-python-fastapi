from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.pet_model import PetModel
from schemas.pet_schema import PetRequestSchema
import repository.pet_repository as pet_repo

def criar_pet(db: Session, pet_dto: PetRequestSchema):
    # Aqui no futuro vamos poder botar regras de negócio. 
    # Exemplo: if pet_dto.idade < 0: raise HTTPException(status_code=400, detail="Idade inválida") excções que iremos colocar.
    return pet_repo.salvar_pet(db, pet_dto)

def listar_pets(db: Session):
    return pet_repo.buscar_todos_pets(db)

def buscar_pet_por_id(db: Session, pet_id: int):
    pet = pet_repo.buscar_pet_por_id(db, pet_id)
    
    # A REGRA DE NEGÓCIO AQUI! Se o Repository não achou, o Service estoura o erro status code de 404 .
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado no sistema.")
    
    return pet

def atualizar_pet(db: Session, pet_id: int, pet_dto: PetRequestSchema):
    # 1. Aqui vamos reutilizar a regra negocio repository, caso nao existe vai explodir erro 404.
    pet_atual = buscar_pet_por_id(db, pet_id)
    
    dados_novos = pet_dto.model_dump(exclude_unset=True)
    
    return pet_repo.atualizar_pet(db, pet_atual, dados_novos)

def deletar_pet(db: Session, pet_id: int):
    # 1. Aqui vamos Validar  se o pet existe (se não existir) vai explodir  o 404)
    pet = buscar_pet_por_id(db, pet_id)
    
    pet_repo.deletar_pet(db, pet)