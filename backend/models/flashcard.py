from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.database import Base


class Flashcard(Base):

    __tablename__ = "flashcards"

    # ============================================================
    # ID
    # ============================================================

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    # ============================================================
    # PERGUNTA
    # ============================================================

    pergunta: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    # ============================================================
    # RESPOSTA
    # ============================================================

    resposta: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    # ============================================================
    # TEMA
    # ============================================================

    tema: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )