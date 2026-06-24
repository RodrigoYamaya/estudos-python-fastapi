from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

# Aqui seria semelhante  a nossa injeção de dependência do banco que se assemlha no java,Vamos injetar objeto externo nessa classe afins de reutilizar os comportamentos desse objeto,que extremamente excencial para o funcionamento dessa classe;
from database.database import get_db 
from schemas.pet_schema import PetRequestSchema
import service.pet_service as pet_service

# Aqui semelhante no java/Spring  @RequestMapping("/pets") no escopo da classe
router = APIRouter(prefix="/pets", tags=["Pets"])


# Equivalente ao @PostMapping
# status.HTTP_201_CREATED garante que a API retorne 201 em vez de 200 ao criar
@router.post("/", status_code=status.HTTP_201_CREATED)
def criar_pet(pet_dto: PetRequestSchema, db: Session = Depends(get_db)):
    # pet_dto é o equivalente ao @RequestBody do Java
    return pet_service.criar_pet(db, pet_dto)


# Equivalente ao @GetMapping
@router.get("/")
def listar_pets(db: Session = Depends(get_db)):
    return pet_service.listar_pets(db)


# Equivalente ao @GetMapping("/{id}")
@router.get("/{pet_id}")
def buscar_pet_por_id(pet_id: int, db: Session = Depends(get_db)):
    # pet_id é o equivalente ao @PathVariable do Javas
    return pet_service.buscar_pet_por_id(db, pet_id)


# Equivalente ao @PutMapping("/{id}")
@router.put("/{pet_id}")
def atualizar_pet(pet_id: int, pet_dto: PetRequestSchema, db: Session = Depends(get_db)):
    return pet_service.atualizar_pet(db, pet_id, pet_dto)


# Equivalente ao @DeleteMapping("/{id}")
# status.HTTP_204_NO_CONTENT é a boa prática para deleção (sucesso, mas sem corpo de resposta)
@router.delete("/{pet_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_pet(pet_id: int, db: Session = Depends(get_db)):
    pet_service.deletar_pet(db, pet_id)