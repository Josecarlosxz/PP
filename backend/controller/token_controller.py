import secrets
from datetime import datetime, timedelta

from backend.database import SessionLocal
from backend.models.token import Token
from backend.models.participante import Participante

def gerar_token(professor_id):
    session = SessionLocal()

    try:
        codigo = secrets.token_urlsafe(8)

        token = Token(
            codigo = codigo,
            ativo = True,
            expira_em = datetime.now() + timedelta(days=30),
            usuario_id = professor_id)
        
        session.add(token)
        session.commit()

        return {
            "mensagem": "Token gerado com sucesso!",
            "codigo": codigo
        }
    
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}
    
    finally:
        session.close()

def entrar(dados):

    session = SessionLocal()

    try:

        resultado = validar_token(session, dados["token"])

        if "erro" in resultado:
            return resultado

        token = resultado["token"]

        participante = Participante(
            nome=dados["nome"],
            token_id=token.id
        )

        session.add(participante)
        session.commit()

        return {
            "mensagem": "Entrada permitida!",
            "participante_id": participante.id,
            "nome": participante.nome,
            "token_id": token.id
        }

    except Exception as e:

        session.rollback()

        return {"erro": str(e)}

    finally:

        session.close()

def validar_token(session, codigo):

    token = (
        session.query(Token)
        .filter(Token.codigo == codigo)
        .first()
    )

    if token is None:
        return {"erro": "Token inválido."}

    if not token.ativo:
        return {"erro": "Token desativado."}

    if token.expira_em < datetime.now():
        return {"erro": "Token expirado."}

    return {"token": token}