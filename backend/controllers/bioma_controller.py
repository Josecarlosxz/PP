from flask import Blueprint, request, jsonify
from backend.database import SessionLocal
from backend.models.bioma import Bioma

bioma_bp = Blueprint("bioma", __name__, url_prefix="/biomas")


@bioma_bp.route("/", methods=["POST"])
def create():
    db = SessionLocal()
    data = request.get_json()

    obj = Bioma(
        nome=data["nome"],
        descricao=data.get("descricao"),
        clima=data["clima"],
        vegetacao=data["vegetacao"]
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    response = {
        "id": obj.id,
        "nome": obj.nome,
        "descricao": obj.descricao,
        "clima": obj.clima,
        "vegetacao": obj.vegetacao
    }

    db.close()
    return jsonify(response)


@bioma_bp.route("/", methods=["GET"])
def get_all():
    db = SessionLocal()
    dados = db.query(Bioma).all()

    response = [{
        "id": b.id,
        "nome": b.nome,
        "descricao": b.descricao,
        "clima": b.clima,
        "vegetacao": b.vegetacao
    } for b in dados]

    db.close()
    return jsonify(response)


@bioma_bp.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    db = SessionLocal()
    obj = db.query(Bioma).filter(Bioma.id == id).first()

    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    response = {
        "id": obj.id,
        "nome": obj.nome,
        "descricao": obj.descricao,
        "clima": obj.clima,
        "vegetacao": obj.vegetacao
    }

    db.close()
    return jsonify(response)


@bioma_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    db = SessionLocal()
    data = request.get_json()

    obj = db.query(Bioma).filter(Bioma.id == id).first()
    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    obj.nome = data.get("nome", obj.nome)
    obj.descricao = data.get("descricao", obj.descricao)
    obj.clima = data.get("clima", obj.clima)
    obj.vegetacao = data.get("vegetacao", obj.vegetacao)

    db.commit()
    db.refresh(obj)

    response = {
        "id": obj.id,
        "nome": obj.nome,
        "descricao": obj.descricao,
        "clima": obj.clima,
        "vegetacao": obj.vegetacao
    }

    db.close()
    return jsonify(response)


@bioma_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    db = SessionLocal()

    obj = db.query(Bioma).filter(Bioma.id == id).first()
    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    bioma_id = obj.id

    db.delete(obj)
    db.commit()
    db.close()

    return jsonify({"msg": "deletado", "id": bioma_id})