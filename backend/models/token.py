from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.database import Base
from datetime import datetime

class Token(Base):
    __tablename__ = "tokens"

    id: Mapped[int] = mapped_column(primary_key=True)
    codigo: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    ativo: Mapped[bool] = mapped_column(Boolean, default=True)
    expira_em: Mapped[datetime] = mapped_column(DateTime)

    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="tokens")
    participantes = relationship("Participante", back_populates="token")