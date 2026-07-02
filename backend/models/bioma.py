from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.database import Base


class Bioma(Base):
    __tablename__ = "biomas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255))
    clima = Column(String(50))
    vegetacao = Column(String(100))

    # N:N com Especie
    especies = relationship(
        "EspecieBioma",
        back_populates="bioma",
        cascade="all, delete-orphan"
    )