from flask import Blueprint, request, jsonify
from backend.database import SessionLocal
from backend.models.usuario import Usuario

usuario_bp = Blueprint("usuario", __name__, url_prefix="/usuarios")


@usuario_bp.route("/", methods=["POST"])
def create():
    db = SessionLocal()
    data = request.get_json()

    obj = Usuario(
        nome=data["nome"],
        email=data["email"],
        senha=data["senha"]
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)

    response = {
        "id": obj.id,
        "nome": obj.nome,
        "email": obj.email
    }

    db.close()
    return jsonify(response)


@usuario_bp.route("/", methods=["GET"])
def get_all():
    db = SessionLocal()
    dados = db.query(Usuario).all()

    response = [{
        "id": u.id,
        "nome": u.nome,
        "email": u.email
    } for u in dados]

    db.close()
    return jsonify(response)


@usuario_bp.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    db = SessionLocal()
    obj = db.query(Usuario).filter(Usuario.id == id).first()

    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    response = {
        "id": obj.id,
        "nome": obj.nome,
        "email": obj.email
    }

    db.close()
    return jsonify(response)


@usuario_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    db = SessionLocal()
    data = request.get_json()

    obj = db.query(Usuario).filter(Usuario.id == id).first()
    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    obj.nome = data.get("nome", obj.nome)
    obj.email = data.get("email", obj.email)
    obj.senha = data.get("senha", obj.senha)

    db.commit()
    db.refresh(obj)

    response = {
        "id": obj.id,
        "nome": obj.nome,
        "email": obj.email
    }

    db.close()
    return jsonify(response)


@usuario_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    db = SessionLocal()

    obj = db.query(Usuario).filter(Usuario.id == id).first()
    if not obj:
        db.close()
        return jsonify({"erro": "não encontrado"}), 404

    user_id = obj.id

    db.delete(obj)
    db.commit()
    db.close()

    return jsonify({"msg": "deletado", "id": user_id})