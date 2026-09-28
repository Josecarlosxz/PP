from flask import Blueprint, jsonify

from backend.database.database import SessionLocal
from backend.models.flashcard import Flashcard
from backend.utils.auth import login_required


flashcard_bp = Blueprint(
    "flashcard",
    __name__,
    url_prefix="/flashcards"
)


# ============================================================
# LISTAR FLASHCARDS
# ============================================================

@flashcard_bp.route("/", methods=["GET"])
@login_required
def get_all():

    db = SessionLocal()

    try:

        flashcards = db.query(Flashcard).all()

        return jsonify([
            {
                "id": flashcard.id,
                "pergunta": flashcard.pergunta,
                "resposta": flashcard.resposta,
                "tema": flashcard.tema
            }
            for flashcard in flashcards
        ]), 200

    finally:

        db.close()


# ============================================================
# BUSCAR FLASHCARD
# ============================================================

@flashcard_bp.route("/<int:id>", methods=["GET"])
@login_required
def get_by_id(id):

    db = SessionLocal()

    try:

        flashcard = (
            db.query(Flashcard)
            .filter(Flashcard.id == id)
            .first()
        )

        if not flashcard:
            return jsonify({
                "erro": "Flashcard não encontrado"
            }), 404

        return jsonify({
            "id": flashcard.id,
            "pergunta": flashcard.pergunta,
            "resposta": flashcard.resposta,
            "tema": flashcard.tema
        }), 200

    finally:

        db.close()