from sqlmodel import Session
from backend.database import engine
from backend.models.animal import Animal

#Create
def cadastrar_animal(dados_formulario):
    #aqui ele recebe os dados preenchidos no forms pelo admin e guarda nas variáveis
    novo_animal = Animal(
        nome_popular=dados_formulario["nome_popular"],
        nome_cientifico=dados_formulario["nome_cientifico"],
        bioma=dados_formulario["bioma"],
        status_extincao=dados_formulario["status_extincao"],
        descricao=dados_formulario["descricao"],
        imagem_url=dados_formulario.get["imagem_url"]
    )

    #Faz a inserção do animal no workbench
    with Session(engine) as sessao:
        sessao.add(novo_animal)
        sessao.commit()
        sessao.refresh(novo_animal)
        
    #Retorna uma mensagem se o animal for adicionado com sucesso
    return {"mensagem": f"{novo_animal.nome_popular} cadastrado com sucesso!", "id": novo_animal.id}

    # Atualizar dados de um animal existente
def atualizar_animal(animal_id: int, dados_formulario: dict):
    with Session(engine) as sessao:
        animal_existente = sessao.get(Animal, animal_id)
        
       
        if not animal_existente:
            return {"erro": "Animal não encontrado para atualização."}
        
        animal_existente.nome_popular = dados_formulario.get("nome_popular", animal_existente.nome_popular)
        animal_existente.nome_cientifico = dados_formulario.get("nome_cientifico", animal_existente.nome_cientifico)
        animal_existente.bioma = dados_formulario.get("bioma", animal_existente.bioma)
        animal_existente.status_extincao = dados_formulario.get("status_extincao", animal_existente.status_extincao)
        animal_existente.descricao = dados_formulario.get("descricao", animal_existente.descricao)
        animal_existente.imagem_url = dados_formulario.get("imagem_url", animal_existente.imagem_url)
        
        sessao.add(animal_existente)
        sessao.commit()
        sessao.refresh(animal_existente)
        
    return {"mensagem": f"{animal_existente.nome_popular} atualizado com sucesso!"}
    
    #delete animal    
def deletar_animal(animal_id: int):
    with Session(engine) as sessao:
        animal_existente = sessao.get(Animal, animal_id)
        if not animal_existente:
            return {"erro": "Animal não encontrado para exclusão."}
        sessao.delete(animal_existente)
        sessao.commit()
        
    return {"mensagem": f"Animal removido com sucesso!"}

    #buscar