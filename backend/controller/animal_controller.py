from backend.database import SessionLocal
from backend.models.animal import Animal
from backend.models.especie import Especie


# =========================
# CADASTRAR ANIMAL
# =========================
def cadastrar_animal(dados_formulario):

    db = SessionLocal()

    try:

        especie = db.query(Especie).filter(
            Especie.id == dados_formulario["especie_id"]
        ).first()

        if not especie:
            return {"erro": "Espécie não encontrada."}

        # impede duplicar animal para mesma espécie (1:1)
        if especie.animal:
            return {"erro": "Essa espécie já possui um animal cadastrado."}

        novo_animal = Animal(
            especie_id=dados_formulario["especie_id"],
            dieta=dados_formulario.get("dieta"),
            habitat_especifico=dados_formulario.get("habitat_especifico")
        )

        db.add(novo_animal)
        db.commit()
        db.refresh(novo_animal)

        return {
            "mensagem": "Animal cadastrado com sucesso!",
            "id": novo_animal.id
        }

    except Exception as erro:
        return {"erro": str(erro)}

    finally:
        db.close()


# =========================
# LISTAR ANIMAIS
# =========================
def listar_animais():

    db = SessionLocal()

    try:

        animais = db.query(Animal).all()

        lista = []

        for animal in animais:
            lista.append({
                "id": animal.id,
                "dieta": animal.dieta,
                "habitat_especifico": animal.habitat_especifico,

                # relacionamento com espécie
                "especie": animal.especie.nome_popular if animal.especie else None
            })

        return {"animais": lista}

    finally:
        db.close()


# =========================
# BUSCAR ANIMAL
# =========================
def buscar_animal(animal_id):

    db = SessionLocal()

    try:

        animal = db.query(Animal).filter(Animal.id == animal_id).first()

        if not animal:
            return {"erro": "Animal não encontrado."}

        return {
            "id": animal.id,
            "dieta": animal.dieta,
            "habitat_especifico": animal.habitat_especifico,
            "especie": animal.especie.nome_popular if animal.especie else None
        }

    finally:
        db.close()


# =========================
# ATUALIZAR ANIMAL
# =========================
def atualizar_animal(animal_id, dados_formulario):

    db = SessionLocal()

    try:

        animal = db.query(Animal).filter(Animal.id == animal_id).first()

        if not animal:
            return {"erro": "Animal não encontrado."}

        animal.dieta = dados_formulario.get("dieta", animal.dieta)
        animal.habitat_especifico = dados_formulario.get("habitat_especifico", animal.habitat_especifico)

        db.commit()
        db.refresh(animal)

        return {"mensagem": "Animal atualizado com sucesso!"}

    except Exception as erro:
        return {"erro": str(erro)}

    finally:
        db.close()


# =========================
# DELETAR ANIMAL
# =========================
def deletar_animal(animal_id):

    db = SessionLocal()

    try:

        animal = db.query(Animal).filter(Animal.id == animal_id).first()

        if not animal:
            return {"erro": "Animal não encontrado."}

        db.delete(animal)
        db.commit()

        return {"mensagem": "Animal removido com sucesso!"}

    except Exception as erro:
        return {"erro": str(erro)}

    finally:
        db.close()