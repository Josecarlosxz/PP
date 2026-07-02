from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from backend.models.especie import Especie


class Animal(Especie):
    __tablename__ = "animais"

    id: Mapped[int] = mapped_column(ForeignKey("especies.id"), primary_key=True)

    dieta: Mapped[str] = mapped_column(String(50))
    habitat_especifico: Mapped[str] = mapped_column(String(100))

    __mapper_args__ = {
        "polymorphic_identity": "animal"
    }
