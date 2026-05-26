from backend.database import SessionLocal
from backend.models.bioma import Bioma



# Essa função recebe os dados do formulário
# e cria um novo bioma no banco de dados.
def cadastrar_bioma(dados_formulario):

    db = SessionLocal()

    try:

        novo_bioma = Bioma(
            nome=dados_formulario["nome"],
            descricao=dados_formulario["descricao"],
            clima=dados_formulario.get("clima"),
            vegetacao=dados_formulario.get("vegetacao")
            )

        db.add(novo_bioma)
        db.commit()
        db.refresh(novo_bioma)
        
        return {"mensagem":f"Bioma '{novo_bioma.nome}'cadastrado com sucesso!","id":novo_bioma.id}

    except Exception as erro:

        return {"erro": str(erro)}

    finally:
        db.close()




# Retorna todos os biomas cadastrados.
def listar_biomas():

    db = SessionLocal()

    try:
        biomas = db.query(Bioma).all()

        lista_biomas = []
        
        #percorre os biomas e adiciona à lista
        for bioma in biomas:

            lista_biomas.append({

                "id": bioma.id,
                "nome": bioma.nome,
                "descricao": bioma.descricao,
                "clima": bioma.clima,
                "vegetacao": bioma.vegetacao,
                # RELATIONSHIP
                # Quantidade de animais relacionadosao bioma
                "quantidade_animais":len(bioma.animais)
                
            })

        return {"biomas": lista_biomas}

    finally:
        db.close()



def buscar_bioma(bioma_id):

    db = SessionLocal()

    try:

        # BUSCA BIOMA PELO ID
        bioma = db.query(Bioma).filter(Bioma.id == bioma_id).first()

        if not bioma:

            return {"erro": "Bioma não encontrado."}

        return {

            "id": bioma.id,
            "nome": bioma.nome,
            "descricao": bioma.descricao,
            "clima": bioma.clima,
            "vegetacao": bioma.vegetacao,

  
            # RELATIONSHIP
            # Lista todos os animais do bioma
            "animais": [
                animal.nome_popular
                for animal in bioma.animais
            ]
        }

    finally:

        db.close()



#
# Atualiza dados de um bioma existente.
def atualizar_bioma(bioma_id, dados_formulario):

    # Abre sessão
    db = SessionLocal()

    try:

        bioma_existente = db.query(Bioma).filter(Bioma.id == bioma_id).first()

        if not bioma_existente:

            return {"erro": "Bioma não encontrado para atualização."}


        # ATUALIZA DADOS
        bioma_existente.nome = dados_formulario.get("nome",bioma_existente.nome)
        bioma_existente.descricao = dados_formulario.get("descricao",bioma_existente.descricao)
        bioma_existente.clima = dados_formulario.get("clima", bioma_existente.clima)
        bioma_existente.vegetacao = dados_formulario.get("vegetacao", bioma_existente.vegetacao)

        db.commit()

        # Atualiza objeto
        db.refresh(bioma_existente)

        return {"mensagem":f"Bioma '{bioma_existente.nome}' atualizado com sucesso!"}

    except Exception as erro:
        return {"erro": str(erro)}

    finally:
        db.close()




# Remove um bioma do banco de dados.
def deletar_bioma(bioma_id):

    db = SessionLocal()

    try:

        bioma_existente = db.query(Bioma).filter(Bioma.id == bioma_id).first()

        if not bioma_existente:
            return {"erro": "Bioma não encontrado para exclusão."}

        db.delete(bioma_existente)

        db.commit()

        return {"mensagem": "Bioma removido com sucesso!"}

    except Exception as erro:
        return {"erro": str(erro)}

    finally:

        db.close()