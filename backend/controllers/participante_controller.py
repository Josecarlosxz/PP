from flask import Blueprint, request, jsonify
from backend.database import SessionLocal
from backend.models.participante import Participante

participante_bp = Blueprint("participante", __name__, url_prefix="/participantes")


@participante_bp.route("/", methods=["POST"])
def create():
    db = SessionLocal()
    data = request.get_json()

    obj = Participante(
        nome=data["nome"],
        token_id=data["token_id"]
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)
    db.close()

    return jsonify({
    "id": obj.id,
    "nome": obj.nome,
    "token_id": obj.token_id
})


@participante_bp.route("/", methods=["GET"])
def get_all():
    db = SessionLocal()
    dados = db.query(Participante).all()
    db.close()

    return jsonify([{
    "id": p.id,
    "nome": p.nome,
    "token_id": p.token_id
} for p in dados])
    
@participante_bp.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    db = SessionLocal()
    obj = db.query(Participante).filter(Participante.id == id).first()
    db.close()

    if not obj:
        return jsonify({"erro": "não encontrado"}), 404

    return jsonify({
    "id": obj.id,
    "nome": obj.nome,
    "token_id": obj.token_id
})

@participante_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    db = SessionLocal()
    data = request.get_json()

    obj = db.query(Participante).filter(Participante.id == id).first()
    if not obj:
        return jsonify({"erro": "não encontrado"}), 404

    obj.nome = data.get("nome", obj.nome)
    obj.token_id = data.get("token_id", obj.token_id)

    db.commit()
    db.refresh(obj)
    db.close()

    return jsonify({
    "id": obj.id,
    "nome": obj.nome,
    "token_id": obj.token_id
})


@participante_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    db = SessionLocal()

    obj = db.query(Participante).filter(Participante.id == id).first()
    if not obj:
        return jsonify({"erro": "não encontrado"}), 404
    
    participante_id = obj.id
    
    db.delete(obj)
    db.commit()
    db.close()

    return jsonify({
    "msg": "deletado",
    "id": participante_id
})