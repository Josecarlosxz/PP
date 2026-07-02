from backend.database import SessionLocal
from backend.models.planta import Planta
from backend.models.especie import Especie


# =========================
# CADASTRAR PLANTA
# =========================
def cadastrar_planta(dados_formulario):

    db = SessionLocal()

    try:

        especie = db.query(Especie).filter(
            Especie.id == dados_formulario["especie_id"]
        ).first()

        if not especie:
            return {"erro": "Espécie não encontrada."}

        # impede duplicar planta para mesma espécie (1:1)
        if especie.planta:
            return {"erro": "Essa espécie já possui uma planta cadastrada."}

        nova_planta = Planta(
            especie_id=dados_formulario["especie_id"],
            tipo_folha=dados_formulario.get("tipo_folha"),
            medicinal=dados_formulario.get("medicinal", False)
        )

        db.add(nova_planta)
        db.commit()
        db.refresh(nova_planta)

        return {
            "mensagem": "Planta cadastrada com sucesso!",
            "id": nova_planta.id
        }

    except Exception as erro:
        return {"erro": str(erro)}

    finally:
        db.close()


# =========================
# LISTAR PLANTAS
# =========================
def listar_plantas():

    db = SessionLocal()

    try:

        plantas = db.query(Planta).all()

        lista = []

        for planta in plantas:
            lista.append({
                "id": planta.id,
                "tipo_folha": planta.tipo_folha,
                "medicinal": planta.medicinal,

                "especie": planta.especie.nome_popular if planta.especie else None
            })

        return {"plantas": lista}

    finally:
        db.close()


# =========================
# BUSCAR PLANTA
# =========================
def buscar_planta(planta_id):

    db = SessionLocal()

    try:

        planta = db.query(Planta).filter(Planta.id == planta_id).first()

        if not planta:
            return {"erro": "Planta não encontrada."}

        return {
            "id": planta.id,
            "tipo_folha": planta.tipo_folha,
            "medicinal": planta.medicinal,
            "especie": planta.especie.nome_popular if planta.especie else None
        }

    finally:
        db.close()


# =========================
# ATUALIZAR PLANTA
# =========================
def atualizar_planta(planta_id, dados_formulario):

    db = SessionLocal()

    try:

        planta = db.query(Planta).filter(Planta.id == planta_id).first()

        if not planta:
            return {"erro": "Planta não encontrada."}

        planta.tipo_folha = dados_formulario.get("tipo_folha", planta.tipo_folha)
        planta.medicinal = dados_formulario.get("medicinal", planta.medicinal)

        db.commit()
        db.refresh(planta)

        return {"mensagem": "Planta atualizada com sucesso!"}

    except Exception as erro:
        return {"erro": str(erro)}

    finally:
        db.close()


# =========================
# DELETAR PLANTA
# =========================
def deletar_planta(planta_id):

    db = SessionLocal()

    try:

        planta = db.query(Planta).filter(Planta.id == planta_id).first()

        if not planta:
            return {"erro": "Planta não encontrada."}

        db.delete(planta)
        db.commit()

        return {"mensagem": "Planta removida com sucesso!"}

    except Exception as erro:
        return {"erro": str(erro)}

    finally:
        db.close()