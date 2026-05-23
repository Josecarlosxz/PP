from sqlmodel import Session

from backend.database import engine
from backend.models.bioma import Bioma


# Create
def cadastrar_bioma(dados_formulario: dict):
    nome = dados_formulario.get("nome")
    if not nome:
        return {"erro": "Campo 'nome' é obrigatório."}

    novo_bioma = Bioma(nome=nome)

    with Session(engine) as sessao:
        sessao.add(novo_bioma)
        sessao.commit()
        sessao.refresh(novo_bioma)

    return {"mensagem": f"Bioma '{novo_bioma.nome}' cadastrado com sucesso!", "id": novo_bioma.id}


# Read (listar)
def listar_biomas():
    with Session(engine) as sessao:
        biomas = sessao.query(Bioma).all()

    return {
        "biomas": [
            {"id": b.id, "nome": b.nome} for b in biomas
        ]
    }


# Read (buscar por id)
def buscar_bioma(bioma_id: int):
    with Session(engine) as sessao:
        bioma = sessao.get(Bioma, bioma_id)

    if not bioma:
        return {"erro": "Bioma não encontrado."}

    return {"id": bioma.id, "nome": bioma.nome}


# Update
def atualizar_bioma(bioma_id: int, dados_formulario: dict):
    with Session(engine) as sessao:
        bioma_existente = sessao.get(Bioma, bioma_id)

        if not bioma_existente:
            return {"erro": "Bioma não encontrado para atualização."}

        novo_nome = dados_formulario.get("nome", bioma_existente.nome)
        bioma_existente.nome = novo_nome

        sessao.add(bioma_existente)
        sessao.commit()
        sessao.refresh(bioma_existente)

    return {"mensagem": f"Bioma '{bioma_existente.nome}' atualizado com sucesso!"}


# Delete
def deletar_bioma(bioma_id: int):
    with Session(engine) as sessao:
        bioma_existente = sessao.get(Bioma, bioma_id)

        if not bioma_existente:
            return {"erro": "Bioma não encontrado para exclusão."}

        sessao.delete(bioma_existente)
        sessao.commit()

    return {"mensagem": "Bioma removido com sucesso!"}

