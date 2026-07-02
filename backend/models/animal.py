from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base


class Animal(Base):
    __tablename__ = "animais"

    id = Column(Integer, primary_key=True, autoincrement=True)

    dieta = Column(String(50))
    habitat_especifico = Column(String(100))

    especie_id = Column(Integer, ForeignKey("especies.id"))

    especie = relationship("Especie", back_populates="animal")