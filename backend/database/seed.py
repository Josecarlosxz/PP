
from backend.database.database import SessionLocal

# ============================================================
# CARREGA OS MODELS
#
# Importante:
# Participante precisa estar registrado antes que o SQLAlchemy
# inicialize os relacionamentos de Token.
# ============================================================

from backend.models.usuario import Usuario
from backend.models.token import Token
from backend.models.participante import Participante
from backend.models.flashcard import Flashcard

from werkzeug.security import generate_password_hash


def criar_admin():

    session = SessionLocal()

    try:

        # ====================================================
        # VERIFICA SE O ADMIN JÁ EXISTE
        # ====================================================

        admin = (
            session.query(Usuario)
            .filter(
                Usuario.email == "admin@biosistema.com"
            )
            .first()
        )

        if admin:

            print("Administrador já existe.")

            return

        # ====================================================
        # CRIA ADMINISTRADOR
        # ====================================================

        admin = Usuario(

            nome="Administrador",

            email="admin@biosistema.com",

            senha_hash=generate_password_hash(
                "admin123"
            ),

            perfil="administrador"

        )

        session.add(admin)

        session.commit()

        session.refresh(admin)

        print("====================================")
        print("Administrador criado com sucesso!")
        print("Email : admin@biosistema.com")
        print("Senha : admin123")
        print("====================================")

    except Exception as e:

        session.rollback()

        print("Erro ao criar administrador:")
        print(e)

    finally:

        session.close()


def criar_flashcards():

    session = SessionLocal()

    try:

        # Verifica se já existem flashcards
        quantidade = session.query(Flashcard).count()

        if quantidade > 0:
            print("Flashcards já existem.")
            return

        flashcards = [
            Flashcard(
                pergunta="O que é biodiversidade?",
                resposta="É a variedade de seres vivos, genes e ecossistemas existentes.",
                tema="Biodiversidade"
            ),

            Flashcard(
                pergunta="O que é um bioma?",
                resposta="É uma grande comunidade ecológica caracterizada por condições ambientais e formas de vida predominantes.",
                tema="Biomas"
            ),

            Flashcard(
                pergunta="O que é uma espécie?",
                resposta="É um grupo de organismos com características semelhantes que podem se reproduzir entre si.",
                tema="Ecologia"
            )
        ]

        session.add_all(flashcards)
        session.commit()

        print("Flashcards criados com sucesso!")

    except Exception as e:

        session.rollback()

        print("Erro ao criar flashcards:")
        print(e)

    finally:

        session.close()

if __name__ == "__main__":

    criar_admin()
    criar_flashcards()