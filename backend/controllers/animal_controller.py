from flask import Blueprint, request, jsonify
from backend.database import SessionLocal
from backend.models.animal import Animal

animal_bp = Blueprint("animal", __name__, url_prefix="/animais")


@animal_bp.route("/", methods=["POST"])
def create():
    db = SessionLocal()
    data = request.get_json()

    obj = Animal(
        nome_popular=data["nome_popular"],
        nome_cientifico=data["nome_cientifico"],
        descricao=data.get("descricao"),
        usuario_id=data["usuario_id"],
        dieta=data["dieta"],
        habitat_especifico=data["habitat_especifico"],
        tipo="animal"
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    response = {
        "id": obj.id,
        "nome_popular": obj.nome_popular,
        "nome_cientifico": obj.nome_cientifico,
        "descricao": obj.descricao,
        "usuario_id": obj.usuario_id,
        "tipo": obj.tipo,
        "dieta": obj.dieta,
        "habitat_especifico": obj.habitat_especifico
    }

    db.close()
    return jsonify(response)


@animal_bp.route("/", methods=["GET"])
def get_all():
    db = SessionLocal()
    dados = db.query(Animal).all()

    response = [{
        "id": a.id,
        "nome_popular": a.nome_popular,
        "nome_cientifico": a.nome_cientifico,
        "descricao": a.descricao,
        "usuario_id": a.usuario_id,
        "dieta": a.dieta,
        "habitat_especifico": a.habitat_especifico
    } for a in dados]

    db.close()
    return jsonify(response)


@animal_bp.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    db = SessionLocal()
    obj = db.query(Animal).filter(Animal.id == id).first()

    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    response = {
        "id": obj.id,
        "nome_popular": obj.nome_popular,
        "nome_cientifico": obj.nome_cientifico,
        "descricao": obj.descricao,
        "usuario_id": obj.usuario_id,
        "tipo": obj.tipo,
        "dieta": obj.dieta,
        "habitat_especifico": obj.habitat_especifico
    }

    db.close()
    return jsonify(response)


@animal_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    db = SessionLocal()
    data = request.get_json()

    obj = db.query(Animal).filter(Animal.id == id).first()
    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    obj.nome_popular = data.get("nome_popular", obj.nome_popular)
    obj.nome_cientifico = data.get("nome_cientifico", obj.nome_cientifico)
    obj.descricao = data.get("descricao", obj.descricao)
    obj.dieta = data.get("dieta", obj.dieta)
    obj.habitat_especifico = data.get("habitat_especifico", obj.habitat_especifico)

    db.commit()
    db.refresh(obj)

    response = {
        "id": obj.id,
        "nome_popular": obj.nome_popular,
        "nome_cientifico": obj.nome_cientifico,
        "descricao": obj.descricao,
        "usuario_id": obj.usuario_id,
        "tipo": obj.tipo,
        "dieta": obj.dieta,
        "habitat_especifico": obj.habitat_especifico
    }

    db.close()
    return jsonify(response)


@animal_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    db = SessionLocal()

    obj = db.query(Animal).filter(Animal.id == id).first()
    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    animal_id = obj.id

    db.delete(obj)
    db.commit()
    db.close()

    return jsonify({"msg": "deletado", "id": animal_id})