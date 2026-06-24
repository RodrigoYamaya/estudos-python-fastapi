from sqlalchemy.orm import Session
from models.pet_model import PetModel
from schemas.pet_schema import PetRequestSchema

# 1. Equivalente ao .save() do Spring Data JPA (INSERT)
def salvar_pet(db: Session, pet_dto: PetRequestSchema):
    # A mágica aplicada! Pega o DTO, transforma em dicionário e injeta na Entidade.
    #O model_dump() pegar objeto no Pydantic que dtos e transformar em dicionario dict(hashmap) que no formato justamento do json que puramento texto(string) ela serve para enviar dados para internet(sair do postman/fromt end) e chega nossa api. Por isso que necessario para conversação dict.
    novo_pet = PetModel(**pet_dto.model_dump())
    
    db.add(novo_pet)
    db.commit()
    db.refresh(novo_pet)
    
    return novo_pet

# 2. Equivalente ao .findAll() do Spring Data JPA
def buscar_todos_pets(db: Session):
    return db.query(PetModel).all()

# 3. Equivalente ao .findById() do Spring Data JPA
def buscar_pet_por_id(db: Session, pet_id: int):
    return db.query(PetModel).filter(PetModel.id == pet_id).first()

# 4. Equivalente ao .save() do Spring Data JPA (UPDATE)
def atualizar_pet(db: Session, pet_atual: PetModel, dados_novos: dict):
    # O Repository não faz IFs nem valida nada. 
    # Ele só recebe o Pet já encontrado e um dicionário com as novidades, e injeta!
    for chave, valor in dados_novos.items():
        setattr(pet_atual, chave, valor)
        
    db.commit()
    db.refresh(pet_atual)
    return pet_atual

# 5. Equivalente ao .delete() do Spring Data JPA
def deletar_pet(db: Session, pet: PetModel):
    # O Repository também não valida se existe. O Service já validou e mandou o objeto certo!
    db.delete(pet)
    db.commit()