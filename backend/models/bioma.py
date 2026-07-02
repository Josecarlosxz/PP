from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.database import Base


class Bioma(Base):
    __tablename__ = "biomas"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str] = mapped_column(String(255))
    clima: Mapped[str] = mapped_column(String(50))
    vegetacao: Mapped[str] = mapped_column(String(100))

    especies = relationship(
        "EspecieBioma",
        back_populates="bioma",
        cascade="all, delete-orphan"
    )