from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base


class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(20), unique=True, nullable=False)
    ativo = Column(Boolean, default=True)
    expira_em = Column(DateTime)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    # relacionamento correto
    usuario = relationship("Usuario", back_populates="tokens")

    participantes = relationship("Participante", back_populates="token")