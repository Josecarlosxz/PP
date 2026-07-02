from sqlalchemy import Column, Integer, ForeignKey
from backend.database import Base
from sqlalchemy.orm import relationship


class EspecieBioma(Base):
    __tablename__ = "especie_bioma"

    id = Column(Integer, primary_key=True, autoincrement=True)

    especie_id = Column(Integer, ForeignKey("especies.id"))
    bioma_id = Column(Integer, ForeignKey("biomas.id"))

    especie = relationship("Especie", back_populates="biomas")
    bioma = relationship("Bioma", back_populates="especies")