from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base


class Planta(Base):
    __tablename__ = "plantas"

    id = Column(Integer, primary_key=True, autoincrement=True)

    tipo_folha = Column(String(50))
    medicinal = Column(Boolean)

    especie_id = Column(Integer, ForeignKey("especies.id"))

    especie = relationship("Especie", back_populates="planta")