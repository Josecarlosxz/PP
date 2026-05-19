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