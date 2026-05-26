from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Float

from backend.database import Base


class Animal(Base):
    __tablename__ = "animais"
    # id gerado pelo banco
    id = Column("id", Integer,primary_key=True, autoincrement=True)
    nome_popular = Column("nome_popular", String(100),nullable=False)
    nome_cientifico= Column("nome_cientifico", String(100),nullable=False)
    especie = Column("especie",String(100),nullable=False)
    peso = Column("peso", Float)
    status_extincao = Column(String(100))
    # texto que será exibido junto ao animal
    descricao= Column("descricao", String(500),nullable=False)
    imagem_url = Column(String(500),nullable=True)


    # UM usuário -> MUITOS animais
    usuario_id = Column(Integer,ForeignKey("usuarios.id"))
    # relacionamento com usuario
    usuario = relationship("Usuario",back_populates="animais")

    # UM bioma -> MUITOS animais
    bioma_id = Column(Integer,ForeignKey("biomas.id"))
    # relacionamento com bioma
    bioma = relationship("Bioma",back_populates="animais")