from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base


class Especie(Base):
    __tablename__ = "especies"

    id = Column(Integer, primary_key=True, autoincrement=True)

    nome_popular = Column(String(100), nullable=False)
    nome_cientifico = Column(String(150), nullable=False)
    descricao = Column(String(255))

    # FK usuário
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    # =========================
    # RELACIONAMENTOS
    # =========================

    usuario = relationship("Usuario", back_populates="especies")

    # 1:1 com Animal
    animal = relationship(
        "Animal",
        back_populates="especie",
        uselist=False
    )

    # 1:1 com Planta
    planta = relationship(
        "Planta",
        back_populates="especie",
        uselist=False
    )

    # N:N com Bioma (via tabela intermediária)
    biomas = relationship(
        "EspecieBioma",
        back_populates="especie",
        cascade="all, delete-orphan"
    )