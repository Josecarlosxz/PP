from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = f"mysql+mysqlconnector://root:root@localhost:3306/pp_fauna"

engine = create_engine(DATABASE_URL, echo=True)

def criar_tabelas():
    from backend.models.animal import Animal
    from backend.models.usuario import Usuario
    
    SQLModel.metadata.create_all(engine)

def obter_sessao():
    with Session(engine) as session:
        yield session