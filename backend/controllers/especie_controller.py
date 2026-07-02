from flask import Blueprint, request, jsonify
from backend.database import SessionLocal
from backend.models.especie import Especie

especie_bp = Blueprint("especie", __name__, url_prefix="/especies")


@especie_bp.route("/", methods=["POST"])
def create():
    db = SessionLocal()
    data = request.get_json()

    obj = Especie(
        nome_popular=data["nome_popular"],
        nome_cientifico=data["nome_cientifico"],
        descricao=data.get("descricao"),
        tipo=data.get("tipo", "especie"),
        usuario_id=data["usuario_id"]
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
        "tipo": obj.tipo
    }

    db.close()
    return jsonify(response)


@especie_bp.route("/", methods=["GET"])
def get_all():
    db = SessionLocal()
    dados = db.query(Especie).all()

    response = [{
        "id": e.id,
        "nome_popular": e.nome_popular,
        "nome_cientifico": e.nome_cientifico,
        "descricao": e.descricao,
        "usuario_id": e.usuario_id,
        "tipo": e.tipo
    } for e in dados]

    db.close()
    return jsonify(response)


@especie_bp.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    db = SessionLocal()
    obj = db.query(Especie).filter(Especie.id == id).first()

    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    response = {
        "id": obj.id,
        "nome_popular": obj.nome_popular,
        "nome_cientifico": obj.nome_cientifico,
        "descricao": obj.descricao,
        "usuario_id": obj.usuario_id,
        "tipo": obj.tipo
    }

    db.close()
    return jsonify(response)


@especie_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    db = SessionLocal()
    data = request.get_json()

    obj = db.query(Especie).filter(Especie.id == id).first()
    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    obj.nome_popular = data.get("nome_popular", obj.nome_popular)
    obj.nome_cientifico = data.get("nome_cientifico", obj.nome_cientifico)
    obj.descricao = data.get("descricao", obj.descricao)

    db.commit()
    db.refresh(obj)

    response = {
        "id": obj.id,
        "nome_popular": obj.nome_popular,
        "nome_cientifico": obj.nome_cientifico,
        "descricao": obj.descricao,
        "usuario_id": obj.usuario_id,
        "tipo": obj.tipo
    }

    db.close()
    return jsonify(response)


@especie_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    db = SessionLocal()

    obj = db.query(Especie).filter(Especie.id == id).first()
    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    eid = obj.id

    db.delete(obj)
    db.commit()
    db.close()

    return jsonify({"msg": "deletado", "id": eid})