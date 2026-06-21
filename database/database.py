import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Carrega as variáveis de ambiente do ficheiro .env
load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# 2. Monta a URL de conexão específica para o MySQL
# O formato é: dialect+driver://username:password@host:port/database
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 3. Cria o motor (repare que removemos o 'check_same_thread', pois era exclusivo do SQLite)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 4. Cria a fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5. Cria a classe Base para as entidades
Base = declarative_base()

# 6. A nossa Injeção de Dependência
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()