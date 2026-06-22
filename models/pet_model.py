from sqlalchemy import Column,Integer,String, Boolean,Double,DateTime

from datetime import datetime

# Importamos a 'Base' que criámos lá no database.py
from database.database import Base

class PetModel(Base):

    __tablename__= "tb_pets"  # O equivalente ao @Table(name = "tb_pets") no java/Spring

   # O equivalente ao @Id e @GeneratedValue(strategy = GenerationType.IDENTITY) do java/Spring
    id = Column(Integer, primary_key= True, index= True)

    # O equivalente ao @Column(nullable = false, length = 50) do java/Spring
    nome = Column(String(50), nullable= False)
    especie = Column(String(50), nullable= False)
    endereco = Column(String(50), nullable= False)
    idade = Column(Integer, nullable= False)
    peso = Column(Double, nullable=False)
    vacinado = Column(Boolean, nullable=False)
    data_cadastro = Column(DateTime, default=datetime.now, nullable=False)
