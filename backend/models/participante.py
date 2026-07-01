from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from backend.database import Base


class Participante(Base):
    __tablename__ = "participantes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    token_id = Column(Integer, ForeignKey("tokens.id"))
    token = relationship("Token")