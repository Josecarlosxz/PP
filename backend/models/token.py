from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base


class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(20), unique=True, nullable=False)
    ativo = Column(Boolean, default=True)
    expira_em = Column(DateTime)
    professor_id = Column(Integer, ForeignKey("usuarios.id"))

    professor = relationship("Usuario", back_populates="tokens")