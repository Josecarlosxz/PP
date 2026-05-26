from backend.database import SessionLocal
from backend.models.animal import Animal



# Essa função recebe os dados vindos do formulário
# e cria um novo animal no banco de dados.
def cadastrar_animal(dados_formulario):

    # ABRE UMA SESSÃO COM O BANCO
    # SessionLocal() cria uma conexão temporária para realizar operações no banco.
    db = SessionLocal()

    try:
        novo_animal = Animal(

            nome_popular=dados_formulario["nome_popular"],
            nome_cientifico=dados_formulario["nome_cientifico"],
            status_extincao=dados_formulario.get("status_extincao"),
            especie=dados_formulario["especie"],
            peso=dados_formulario.get("peso"),
            descricao=dados_formulario["descricao"],
            imagem_url=dados_formulario.get("imagem_url"),
            # ID do usuário dono do animal
            usuario_id=dados_formulario["usuario_id"],
            # ID do bioma do animal
            bioma_id=dados_formulario["bioma_id"]
        )

        # adiciona obejeto na sessao
        db.add(novo_animal)
        # salva as alterações no banco
        db.commit()
        # atualiza objeto
        db.refresh(novo_animal)


        return {"mensagem":f"{novo_animal.nome_popular} cadastrado com sucesso!", "id":novo_animal.id}

    # caso tenha erro
    except Exception as erro:
        return {"erro": str(erro)}

    # fecha conexão com o banco
    finally:
        db.close()



# Atualiza os dados de um animal já existente.
def atualizar_animal(animal_id, dados_formulario):
    # Abre sessão
    db = SessionLocal()

    try:

        # BUSCA O ANIMAL PELO ID
        animal_existente = db.query(Animal).filter(Animal.id == animal_id).first()

        if not animal_existente:
            return {"erro": "Animal não encontrado para atualização."}


        # ATUALIZA CADA CAMPO
        animal_existente.nome_popular = dados_formulario.get("nome_popular", animal_existente.nome_popular)
        animal_existente.nome_cientifico = dados_formulario.get("nome_cientifico", animal_existente.nome_cientifico)
        animal_existente.status_extincao = dados_formulario.get("status_extincao",animal_existente.status_extincao)
        animal_existente.especie = dados_formulario.get("especie",animal_existente.especie)
        animal_existente.peso = dados_formulario.get("peso",animal_existente.peso)
        animal_existente.descricao = dados_formulario.get("descricao",animal_existente.descricao)
        animal_existente.imagem_url = dados_formulario.get("imagem_url",animal_existente.imagem_url)

        # Atualiza Foreign Key do usuário
        animal_existente.usuario_id = dados_formulario.get("usuario_id", animal_existente.usuario_id)

        # Atualiza Foreign Key do bioma
        animal_existente.bioma_id = dados_formulario.get("bioma_id",animal_existente.bioma_id)

        # SALVA ALTERAÇÕES
        db.commit()

        # Atualiza objeto
        db.refresh(animal_existente)

        return {"mensagem":f"{animal_existente.nome_popular} atualizado com sucesso!"}

    except Exception as erro:
        return {"erro": str(erro)}

    finally:
        db.close()



# FUNÇÃO: DELETAR ANIMAL
def deletar_animal(animal_id):

    # Abre sessão
    db = SessionLocal()

    try:
        animal_existente = db.query(Animal).filter(Animal.id == animal_id).first()

        if not animal_existente:

            return {"erro": "Animal não encontrado para exclusão."}


        db.delete(animal_existente)
        db.commit()

        return {"mensagem": "Animal removido com sucesso!"}

    except Exception as erro:
        return {"erro": str(erro)}

    finally:

        db.close()



# Retorna todos os animais cadastrados.
def listar_animais():

    # Abre sessão
    db = SessionLocal()

    try:


        # BUSCA TODOS OS ANIMAIS
        animais = db.query(Animal).all()

        # Lista que armazenará os resultados
        lista_animais = []


        for animal in animais:

            lista_animais.append({
                "id": animal.id,
                "nome_popular": animal.nome_popular,
                "nome_cientifico": animal.nome_cientifico,
                "especie": animal.especie,
                "peso": animal.peso,
                "descricao": animal.descricao,
                "imagem_url": animal.imagem_url,

                # RELATIONSHIP
                # Acessa dados das tabelas relacionadas
                "usuario": animal.usuario.nome,

                "bioma": animal.bioma.nome
            })

        # Retorna lista
        return lista_animais

    finally:

        db.close()


# FUNÇÃO: BUSCAR ANIMAL
def buscar_animal(animal_id):

    # Abre sessão
    db = SessionLocal()

    try:
        animal = db.query(Animal).filter( Animal.id == animal_id).first()

        if not animal:

            return {"erro": "Animal não encontrado."}

        return {

            "id": animal.id,
            "nome_popular": animal.nome_popular,
            "nome_cientifico": animal.nome_cientifico,
            "especie": animal.especie,
            "peso": animal.peso,
            "descricao": animal.descricao,
            "imagem_url": animal.imagem_url,
            # Dados do relacionamento
            "usuario": animal.usuario.nome,
            "bioma": animal.bioma.nome
        }

    finally:

        db.close()