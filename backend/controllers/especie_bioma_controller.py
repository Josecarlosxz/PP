from flask import Blueprint, request, jsonify
from backend.database import SessionLocal
from backend.models.especie_bioma import EspecieBioma

especie_bioma_bp = Blueprint("especie_bioma", __name__, url_prefix="/especie-bioma")


@especie_bioma_bp.route("/", methods=["POST"])
def create():
    db = SessionLocal()
    data = request.get_json()

    obj = EspecieBioma(
        especie_id=data["especie_id"],
        bioma_id=data["bioma_id"]
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    response = {
        "id": obj.id,
        "especie_id": obj.especie_id,
        "bioma_id": obj.bioma_id
    }

    db.close()
    return jsonify(response)


@especie_bioma_bp.route("/", methods=["GET"])
def get_all():
    db = SessionLocal()
    dados = db.query(EspecieBioma).all()

    response = [{
        "id": d.id,
        "especie_id": d.especie_id,
        "bioma_id": d.bioma_id
    } for d in dados]

    db.close()
    return jsonify(response)


@especie_bioma_bp.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    db = SessionLocal()
    obj = db.query(EspecieBioma).filter(EspecieBioma.id == id).first()

    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    response = {
        "id": obj.id,
        "especie_id": obj.especie_id,
        "bioma_id": obj.bioma_id
    }

    db.close()
    return jsonify(response)


@especie_bioma_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    db = SessionLocal()
    data = request.get_json()

    obj = db.query(EspecieBioma).filter(EspecieBioma.id == id).first()
    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    obj.especie_id = data.get("especie_id", obj.especie_id)
    obj.bioma_id = data.get("bioma_id", obj.bioma_id)

    db.commit()
    db.refresh(obj)

    response = {
        "id": obj.id,
        "especie_id": obj.especie_id,
        "bioma_id": obj.bioma_id
    }

    db.close()
    return jsonify(response)


@especie_bioma_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    db = SessionLocal()

    obj = db.query(EspecieBioma).filter(EspecieBioma.id == id).first()
    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    eid = obj.id

    db.delete(obj)
    db.commit()
    db.close()

    return jsonify({"msg": "deletado", "id": eid})