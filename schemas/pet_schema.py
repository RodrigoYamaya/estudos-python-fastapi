from pydantic import BaseModel
from datetime import datetime

class PetRequestSchema(BaseModel):
    nome: str
    especie: str
    endereco: str
    idade: int
    peso: float  # No Pydantic, o Double do banco mapeia para 'float' no Python,Diferentemente no java;
    vacinado: bool

# Aqui e o DTO DE SAIDA, Sgue o principio de Herença em POO, Vai herdar tudo dos atributos PetRequestSchema.
# Aqui e muito diferente do java/Spring que la usamos CLASSE "RECORDS" e usamos mapstruct para converter os dtos para entidade;
#Ja aqui usamos Herança que nao necessita do Mapstrcut que pydantic foi desenvolvido para ser assim!!
class PetResponseSchema(PetRequestSchema):

    id:int 
    data_cadastro: datetime

    # Esta configuração é obrigatória para o Pydantic conseguir ler a classe do SQLAlchemy
    class Config:
        from_attributes = True
