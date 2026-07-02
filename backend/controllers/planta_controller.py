from flask import Blueprint, request, jsonify
from backend.database import SessionLocal
from backend.models.planta import Planta

planta_bp = Blueprint("planta", __name__, url_prefix="/plantas")


@planta_bp.route("/", methods=["POST"])
def create():
    db = SessionLocal()
    data = request.get_json()

    obj = Planta(
        nome_popular=data["nome_popular"],
        nome_cientifico=data["nome_cientifico"],
        descricao=data["descricao"],
        usuario_id=data["usuario_id"],
        tipo_folha=data["tipo_folha"],
        medicinal=data["medicinal"],
        tipo="planta"
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
        "tipo_folha": obj.tipo_folha,
        "medicinal": obj.medicinal
    }

    db.close()
    return jsonify(response)


@planta_bp.route("/", methods=["GET"])
def get_all():
    db = SessionLocal()
    dados = db.query(Planta).all()

    response = [{
        "id": p.id,
        "nome_popular": p.nome_popular,
        "nome_cientifico": p.nome_cientifico,
        "descricao": p.descricao,
        "usuario_id": p.usuario_id,
        "tipo": p.tipo,
        "tipo_folha": p.tipo_folha,
        "medicinal": p.medicinal
    } for p in dados]

    db.close()
    return jsonify(response)


@planta_bp.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    db = SessionLocal()
    obj = db.query(Planta).filter(Planta.id == id).first()

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
        "tipo_folha": obj.tipo_folha,
        "medicinal": obj.medicinal
    }

    db.close()
    return jsonify(response)


@planta_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    db = SessionLocal()
    data = request.get_json()

    obj = db.query(Planta).filter(Planta.id == id).first()
    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    obj.nome_popular = data.get("nome_popular", obj.nome_popular)
    obj.nome_cientifico = data.get("nome_cientifico", obj.nome_cientifico)
    obj.descricao = data.get("descricao", obj.descricao)
    obj.tipo_folha = data.get("tipo_folha", obj.tipo_folha)
    obj.medicinal = data.get("medicinal", obj.medicinal)

    db.commit()
    db.refresh(obj)

    response = {
        "id": obj.id,
        "nome_popular": obj.nome_popular,
        "nome_cientifico": obj.nome_cientifico,
        "descricao": obj.descricao,
        "usuario_id": obj.usuario_id,
        "tipo": obj.tipo,
        "tipo_folha": obj.tipo_folha,
        "medicinal": obj.medicinal
    }

    db.close()
    return jsonify(response)


@planta_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    db = SessionLocal()

    obj = db.query(Planta).filter(Planta.id == id).first()
    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    planta_id = obj.id

    db.delete(obj)
    db.commit()
    db.close()

    return jsonify({"msg": "deletado", "id": planta_id})