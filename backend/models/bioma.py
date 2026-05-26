from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base


class Bioma(Base):
    __tablename__ = "biomas"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome" , String(100) , nullable=False)
    descricao = Column("descricao", String(255) , nullable=False)
    clima = Column("clima", String(100))
    vegetacao = Column("vegetacao", String(100))
    

    # UM bioma pode possuir MUITOS animais -> RELACIONAMENTO 1:N
    animais = relationship("Animal", back_populates="bioma")

    