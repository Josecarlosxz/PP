from backend.database import SessionLocal
from backend.models.especie import Especie
from backend.models.usuario import Usuario


# =========================
# CRIAR ESPÉCIE
# =========================
def cadastrar_especie(dados_formulario):

    db = SessionLocal()

    try:

        usuario = db.query(Usuario).filter(
            Usuario.id == dados_formulario["usuario_id"]
        ).first()

        if not usuario:
            return {"erro": "Usuário não encontrado."}

        nova_especie = Especie(
            nome_popular=dados_formulario["nome_popular"],
            nome_cientifico=dados_formulario["nome_cientifico"],
            peso=dados_formulario.get("peso"),
            descricao=dados_formulario["descricao"],
            imagem_url=dados_formulario.get("imagem_url"),
            status_extincao=dados_formulario.get("status_extincao"),
            usuario_id=dados_formulario["usuario_id"]
        )

        db.add(nova_especie)
        db.commit()
        db.refresh(nova_especie)

        return {
            "mensagem": f"Espécie '{nova_especie.nome_popular}' cadastrada com sucesso!",
            "id": nova_especie.id
        }

    except Exception as erro:
        return {"erro": str(erro)}

    finally:
        db.close()


# =========================
# LISTAR ESPÉCIES
# =========================
def listar_especies():

    db = SessionLocal()

    try:

        especies = db.query(Especie).all()

        lista = []

        for especie in especies:
            lista.append({
                "id": especie.id,
                "nome_popular": especie.nome_popular,
                "nome_cientifico": especie.nome_cientifico,
                "peso": especie.peso,
                "descricao": especie.descricao,
                "imagem_url": especie.imagem_url,
                "status_extincao": especie.status_extincao,

                # RELAÇÃO 1:N
                "usuario": especie.usuario.nome if especie.usuario else None,

                # RELAÇÃO N:N (Biomas)
                "biomas": [
                    eb.bioma.nome for eb in especie.biomas
                ],

                # RELAÇÃO 1:1 (NOVO)
                "animal": especie.animal.id if especie.animal else None,
                "planta": especie.planta.id if especie.planta else None
            })

        return {"especies": lista}

    finally:
        db.close()


# =========================
# BUSCAR ESPÉCIE
# =========================
def buscar_especie(especie_id):

    db = SessionLocal()

    try:

        especie = db.query(Especie).filter(
            Especie.id == especie_id
        ).first()

        if not especie:
            return {"erro": "Espécie não encontrada."}

        return {
            "id": especie.id,
            "nome_popular": especie.nome_popular,
            "nome_cientifico": especie.nome_cientifico,
            "peso": especie.peso,
            "descricao": especie.descricao,
            "imagem_url": especie.imagem_url,
            "status_extincao": especie.status_extincao,

            # USUÁRIO
            "usuario": especie.usuario.nome if especie.usuario else None,

            # BIOMAS
            "biomas": [
                eb.bioma.nome for eb in especie.biomas
            ],

            # 1:1
            "animal": {
                "id": especie.animal.id,
                "dieta": especie.animal.dieta,
                "habitat": especie.animal.habitat_especifico
            } if especie.animal else None,

            "planta": {
                "id": especie.planta.id,
                "tipo_folha": especie.planta.tipo_folha,
                "medicinal": especie.planta.medicinal
            } if especie.planta else None
        }

    finally:
        db.close()


# =========================
# ATUALIZAR ESPÉCIE
# =========================
def atualizar_especie(especie_id, dados_formulario):

    db = SessionLocal()

    try:

        especie = db.query(Especie).filter(
            Especie.id == especie_id
        ).first()

        if not especie:
            return {"erro": "Espécie não encontrada."}

        especie.nome_popular = dados_formulario.get("nome_popular", especie.nome_popular)
        especie.nome_cientifico = dados_formulario.get("nome_cientifico", especie.nome_cientifico)
        especie.peso = dados_formulario.get("peso", especie.peso)
        especie.descricao = dados_formulario.get("descricao", especie.descricao)
        especie.imagem_url = dados_formulario.get("imagem_url", especie.imagem_url)
        especie.status_extincao = dados_formulario.get("status_extincao", especie.status_extincao)

        db.commit()
        db.refresh(especie)

        return {
            "mensagem": f"Espécie '{especie.nome_popular}' atualizada com sucesso!"
        }

    except Exception as erro:
        return {"erro": str(erro)}

    finally:
        db.close()


# =========================
# DELETAR ESPÉCIE
# =========================
def deletar_especie(especie_id):

    db = SessionLocal()

    try:

        especie = db.query(Especie).filter(
            Especie.id == especie_id
        ).first()

        if not especie:
            return {"erro": "Espécie não encontrada."}

        db.delete(especie)
        db.commit()

        return {"mensagem": "Espécie removida com sucesso!"}

    except Exception as erro:
        return {"erro": str(erro)}

    finally:
        db.close()