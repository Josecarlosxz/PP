from typing import Optional
from sqlmodel import Field, SQLModel

# a inserção de animais só será permitida se o usuário estiver como admin
class Animal(SQLModel, table=True):
    # id gerado pelo banco
    id: Optional[int] = Field(default=None, primary_key=True)
    nome_popular: str = Field(index=True, max_length=100)
    nome_cientifico: str = Field(max_length=100)
    # qual bioma ele hábita
    bioma: str = Field(max_length=50)
    status_extincao: str = Field(default="Pouco preocupante", max_length=50)
    # texto que será exibido junto ao animal
    descricao: str
    imagem_url: Optional[str] = Field(default=None, max_length=500)
