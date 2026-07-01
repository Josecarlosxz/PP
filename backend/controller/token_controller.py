import secrets
from datetime import datetime, timedelta

from backend.database import SessionLocal
from backend.models.token import Token

def gerar_token(professor_id):
    session = SessionLocal()

    try:
        codigo = secrets.token_urlsafe(8)

        token = Token(
            codigo = codigo,
            ativo = True,
            expira_em = datetime.now + timedelta(days=30),
            professor_id = professor_id)
        
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