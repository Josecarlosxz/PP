from flask import Blueprint, request, jsonify
from backend.database import SessionLocal
from backend.models.token import Token
from datetime import datetime

token_bp = Blueprint("token", __name__, url_prefix="/tokens")


@token_bp.route("/", methods=["POST"])
def create():
    db = SessionLocal()
    data = request.get_json()

    obj = Token(
        codigo=data["codigo"],
        ativo=data["ativo"],
        expira_em=datetime.fromisoformat(data["expira_em"]),
        usuario_id=data["usuario_id"]
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    response = {
        "id": obj.id,
        "codigo": obj.codigo,
        "ativo": obj.ativo,
        "expira_em": obj.expira_em.isoformat(),
        "usuario_id": obj.usuario_id
    }

    db.close()
    return jsonify(response)


@token_bp.route("/", methods=["GET"])
def get_all():
    db = SessionLocal()
    dados = db.query(Token).all()

    response = [{
        "id": t.id,
        "codigo": t.codigo,
        "ativo": t.ativo,
        "expira_em": t.expira_em,
        "usuario_id": t.usuario_id
    } for t in dados]

    db.close()
    return jsonify(response)


@token_bp.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    db = SessionLocal()
    obj = db.query(Token).filter(Token.id == id).first()

    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    response = {
        "id": obj.id,
        "codigo": obj.codigo,
        "ativo": obj.ativo,
        "expira_em": obj.expira_em,
        "usuario_id": obj.usuario_id
    }

    db.close()
    return jsonify(response)


@token_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    db = SessionLocal()
    data = request.get_json()

    obj = db.query(Token).filter(Token.id == id).first()
    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    obj.codigo = data.get("codigo", obj.codigo)
    obj.ativo = data.get("ativo", obj.ativo)

    if "expira_em" in data:
        obj.expira_em = datetime.fromisoformat(data["expira_em"])

    db.commit()
    db.refresh(obj)

    response = {
        "id": obj.id,
        "codigo": obj.codigo,
        "ativo": obj.ativo,
        "expira_em": obj.expira_em.isoformat(),
        "usuario_id": obj.usuario_id
    }

    db.close()
    return jsonify(response)


@token_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    db = SessionLocal()

    obj = db.query(Token).filter(Token.id == id).first()
    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    token_id = obj.id

    db.delete(obj)
    db.commit()
    db.close()

    return jsonify({"msg": "deletado", "id": token_id})