from typing import Optional

from sqlmodel import Field, SQLModel


class Bioma(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(max_length=80, index=True, unique=True)

