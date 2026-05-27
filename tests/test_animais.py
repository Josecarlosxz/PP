from main import app

client = app.test_client()


def test_criar_animal():
    response = client.post("/animais", data={
        "nome_popular": "Leão",
        "nome_cientifico": "Panthera leo",
        "especie": "Mamífero",
        "descricao": "Animal selvagem",
        "usuario_id": "1",
        "bioma_id": "1"
    })

    assert response.status_code == 200
    assert "Sucesso" in response.data.decode()


def test_listar_animais():
    response = client.get("/animais")

    assert response.status_code == 200


def test_buscar_animal():
    response = client.get("/animais/1")

    assert response.status_code == 200


def test_atualizar_animal():
    response = client.post("/animais/1", data={
        "nome": "Leão Atualizado",
        "idade": "6"
    })

    assert response.status_code == 200
    assert "Sucesso" in response.data.decode()


def test_deletar_animal():
    response = client.post("/animais/1/deletar")

    assert response.status_code == 200
    assert "Sucesso" in response.data.decode()