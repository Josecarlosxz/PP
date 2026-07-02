from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(100))

    # 1:N -> usuário pode cadastrar várias espécies
    especies = relationship("Especie", back_populates="usuario")

    # 1:N -> tokens do usuário
    tokens = relationship("Token", back_populates="usuario")