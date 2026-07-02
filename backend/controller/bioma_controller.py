from backend.database import SessionLocal
from backend.models.bioma import Bioma


# =========================
# CRIAR BIOMA
# =========================
def cadastrar_bioma(dados_formulario):

    db = SessionLocal()

    try:

        novo_bioma = Bioma(
            nome=dados_formulario["nome"],
            descricao=dados_formulario["descricao"],
            clima=dados_formulario.get("clima"),
            vegetacao=dados_formulario.get("vegetacao")
        )

        db.add(novo_bioma)
        db.commit()
        db.refresh(novo_bioma)

        return {
            "mensagem": f"Bioma '{novo_bioma.nome}' cadastrado com sucesso!",
            "id": novo_bioma.id
        }

    except Exception as erro:
        return {"erro": str(erro)}

    finally:
        db.close()


# =========================
# LISTAR BIOMAS
# =========================
def listar_biomas():

    db = SessionLocal()

    try:

        biomas = db.query(Bioma).all()

        lista = []

        for bioma in biomas:

            lista.append({
                "id": bioma.id,
                "nome": bioma.nome,
                "descricao": bioma.descricao,
                "clima": bioma.clima,
                "vegetacao": bioma.vegetacao,

                # RELAÇÃO N:N (Bioma → EspecieBioma → Especie)
                "quantidade_especies": len(bioma.especies) if bioma.especies else 0
            })

        return {"biomas": lista}

    finally:
        db.close()


# =========================
# BUSCAR BIOMA
# =========================
def buscar_bioma(bioma_id):

    db = SessionLocal()

    try:

        bioma = db.query(Bioma).filter(Bioma.id == bioma_id).first()

        if not bioma:
            return {"erro": "Bioma não encontrado."}

        return {
            "id": bioma.id,
            "nome": bioma.nome,
            "descricao": bioma.descricao,
            "clima": bioma.clima,
            "vegetacao": bioma.vegetacao,

            # ESPÉCIES RELACIONADAS
            "especies": [
                eb.especie.nome_popular
                for eb in bioma.especies
            ] if bioma.especies else []
        }

    finally:
        db.close()


# =========================
# ATUALIZAR BIOMA
# =========================
def atualizar_bioma(bioma_id, dados_formulario):

    db = SessionLocal()

    try:

        bioma = db.query(Bioma).filter(Bioma.id == bioma_id).first()

        if not bioma:
            return {"erro": "Bioma não encontrado para atualização."}

        bioma.nome = dados_formulario.get("nome", bioma.nome)
        bioma.descricao = dados_formulario.get("descricao", bioma.descricao)
        bioma.clima = dados_formulario.get("clima", bioma.clima)
        bioma.vegetacao = dados_formulario.get("vegetacao", bioma.vegetacao)

        db.commit()
        db.refresh(bioma)

        return {
            "mensagem": f"Bioma '{bioma.nome}' atualizado com sucesso!"
        }

    except Exception as erro:
        return {"erro": str(erro)}

    finally:
        db.close()


# =========================
# DELETAR BIOMA
# =========================
def deletar_bioma(bioma_id):

    db = SessionLocal()

    try:

        bioma = db.query(Bioma).filter(Bioma.id == bioma_id).first()

        if not bioma:
            return {"erro": "Bioma não encontrado para exclusão."}

        db.delete(bioma)
        db.commit()

        return {"mensagem": "Bioma removido com sucesso!"}

    except Exception as erro:
        return {"erro": str(erro)}

    finally:
        db.close()