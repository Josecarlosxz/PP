from main import app

client = app.test_client()

# =========================
# IDs globais (IMPORTANTE)
# =========================
usuario_id = None
especie_id = None
animal_id = None
planta_id = None


# =========================
# USUÁRIO
# =========================
def test_criar_usuario():
    global usuario_id

    response = client.post("/usuarios", data={
        "nome": "João",
        "email": "joao_teste@email.com",
        "senha": "123"
    })

    assert response.status_code == 200
    assert "Sucesso" in response.data.decode()

    usuario_id = 1  # ou pegar do retorno se quiser evoluir


# =========================
# ESPÉCIE
# =========================
def test_criar_especie():
    global especie_id

    response = client.post("/especies", data={
        "nome_popular": "Onça",
        "nome_cientifico": "Panthera onca",
        "descricao": "Felino grande",
        "status_extincao": "vulneravel",
        "usuario_id": str(usuario_id)
    })

    assert response.status_code == 200
    assert "Sucesso" in response.data.decode()

    especie_id = 1


def test_listar_especies():
    response = client.get("/especies")
    assert response.status_code == 200


def test_buscar_especie():
    response = client.get(f"/especies/{especie_id}")
    assert response.status_code == 200


def test_atualizar_especie():
    response = client.post(f"/especies/{especie_id}", data={
        "nome_popular": "Onça Atualizada"
    })

    assert response.status_code == 200


# =========================
# ANIMAL
# =========================
def test_criar_animal():
    global animal_id

    response = client.post("/animais", data={
        "especie_id": str(especie_id),
        "dieta": "carnivoro",
        "habitat_especifico": "floresta"
    })

    assert response.status_code == 200
    assert "Sucesso" in response.data.decode()

    animal_id = 1


def test_buscar_animal():
    response = client.get(f"/animais/{animal_id}")
    assert response.status_code == 200


def test_atualizar_animal():
    response = client.post(f"/animais/{animal_id}", data={
        "dieta": "onivoro"
    })

    assert response.status_code == 200


def test_deletar_animal():
    response = client.post(f"/animais/{animal_id}/deletar")
    assert response.status_code == 200


# =========================
# PLANTA
# =========================
def test_criar_planta():
    global planta_id

    response = client.post("/plantas", data={
        "especie_id": str(especie_id),
        "tipo_folha": "larga",
        "medicinal": "true"
    })

    assert response.status_code == 200

    planta_id = 1


def test_buscar_planta():
    response = client.get(f"/plantas/{planta_id}")
    assert response.status_code == 200


def test_deletar_planta():
    response = client.post(f"/plantas/{planta_id}/deletar")
    assert response.status_code == 200


# =========================
# BIOMA
# =========================
def test_criar_bioma():
    response = client.post("/biomas", data={
        "nome": "Amazônia",
        "descricao": "Floresta tropical",
        "clima": "quente",
        "vegetacao": "densa"
    })

    assert response.status_code == 200


def test_deletar_especie():
    response = client.post(f"/especies/{especie_id}/deletar")
    assert response.status_code == 200


def test_deletar_planta():
    response = client.post(f"/plantas/{planta_id}/deletar")
    assert response.status_code == 200


def test_deletar_bioma():
    response = client.post("/biomas/1/deletar")
    assert response.status_code == 200