from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    senha: Mapped[str] = mapped_column(String(100))

    especies = relationship("Especie", back_populates="usuario")
    tokens = relationship("Token", back_populates="usuario")