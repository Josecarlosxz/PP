from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.database import Base


class EspecieBioma(Base):
    __tablename__ = "especie_bioma"

    id: Mapped[int] = mapped_column(primary_key=True)

    especie_id: Mapped[int] = mapped_column(ForeignKey("especies.id"))
    bioma_id: Mapped[int] = mapped_column(ForeignKey("biomas.id"))

    especie = relationship("Especie", back_populates="biomas")
    bioma = relationship("Bioma", back_populates="especies")