
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///meubanco.db"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker( autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# def criar_tabelas():
#     from backend.models.animal import Animal
#     from backend.models.usuario import Usuario
#     from backend.models.bioma import Bioma

#     SQLModel.metadata.create_all(engine)

# def obter_sessao():
#     with Session(engine) as session:
#         yield session