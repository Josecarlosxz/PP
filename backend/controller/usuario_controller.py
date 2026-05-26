from backend.database import SessionLocal
from backend.models.usuario import Usuario



def cadastrar_usuario(dados_formulario):

    # abre sessão com banco
    db = SessionLocal()

    try:
        usuario_existente = db.query(Usuario).filter(Usuario.email == dados_formulario["email"]).first()

        if usuario_existente:
            return {
                "erro": "Esse email já está cadastrado."
            }

        novo_usuario = Usuario(
            nome=dados_formulario["nome"],
            email=dados_formulario["email"],
            senha=dados_formulario["senha"]
        )

        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)

        return {
            "mensagem":
            f"Usuário '{novo_usuario.nome}' cadastrado com sucesso!",
            "id":
            novo_usuario.id
        }

    except Exception as erro:

        return {
            "erro": str(erro)
        }

    finally:
        
        db.close()



def listar_usuarios():
    db = SessionLocal()
    
    try:

        usuarios = db.query(Usuario).all()

        lista_usuarios = []

        for usuario in usuarios:
            lista_usuarios.append({
                "id": usuario.id,
                "nome": usuario.nome,
                "email": usuario.email,
                # relationship()
                # usuario.animais acessa todos os animais do usuário
                "animais": [

                    {
                        "id": animal.id,
                        "nome_popular": animal.nome_popular
                    }

                    for animal in usuario.animais
                ]
            })

        return {
            "usuarios": lista_usuarios
        }

    except Exception as erro:

        return {
            "erro": str(erro)
        }

    finally:

        db.close()


def buscar_usuario(usuario_id):

    db = SessionLocal()

    try:

        # busca usuário pelo ID
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()

        if not usuario:
            return {
                "erro": "Usuário não encontrado."
            }

        return {
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            
            # relationship()
            "animais": [

                {
                    "id": animal.id,
                    "nome_popular": animal.nome_popular
                }

                for animal in usuario.animais
            ]
        }

    except Exception as erro:

        return {
            "erro": str(erro)
        }

    finally:

        db.close()


def atualizar_usuario(usuario_id, dados_formulario):


    db = SessionLocal()

    try:

        # busca usuário
        usuario_existente = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        
        if not usuario_existente:
            return {
                "erro": "Usuário não encontrado para atualização."
            }

 
        # verifica se email já existe para outro usuário
        novo_email = dados_formulario.get("email")

        if novo_email:
            email_existente = db.query(Usuario).filter(
                Usuario.email == novo_email,
                Usuario.id != usuario_id
            ).first()

            if email_existente:
                return {
                    "erro": "Esse email já está sendo usado."
                }

   
        usuario_existente.nome = dados_formulario.get("nome",usuario_existente.nome)
        usuario_existente.email = dados_formulario.get("email",usuario_existente.email)
        usuario_existente.senha = dados_formulario.get("senha",usuario_existente.senha)

        db.commit()
        db.refresh(usuario_existente)

        return {

            "mensagem":
            f"Usuário '{usuario_existente.nome}' atualizado com sucesso!"
        }

    except Exception as erro:

        return {
            "erro": str(erro)
        }

    finally:

        db.close()


def deletar_usuario(usuario_id):

    db = SessionLocal()

    try:


        usuario_existente = db.query(Usuario).filter(
            Usuario.id == usuario_id
        ).first()

        if not usuario_existente:

            return {
                "erro": "Usuário não encontrado para exclusão."
            }

        # remove usuário
        db.delete(usuario_existente)

        # executa delete
        db.commit()

        return {
            "mensagem": "Usuário removido com sucesso!"
        }

    except Exception as erro:

        return {
            "erro": str(erro)
        }

    finally:


        db.close()