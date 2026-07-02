def test_animal_crud(client):
    # =========================
    # CREATE
    # =========================
    res = client.post("/animais/", json={
        "nome_popular": "Leão",
        "nome_cientifico": "Panthera leo",
        "descricao": "Felino",
        "usuario_id": 1,
        "dieta": "carnívoro",
        "habitat_especifico": "savana"
    })

    assert res.status_code == 200

    data = res.get_json()
    assert data is not None
    assert "id" in data

    animal_id = data["id"]

    assert data["nome_popular"] == "Leão"
    assert data["dieta"] == "carnívoro"
    assert data["habitat_especifico"] == "savana"

    # =========================
    # READ
    # =========================
    res = client.get(f"/animais/{animal_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["id"] == animal_id
    assert data["nome_popular"] == "Leão"
    assert data["descricao"] == "Felino"
    assert data["dieta"] == "carnívoro"

    # =========================
    # UPDATE
    # =========================
    res = client.put(f"/animais/{animal_id}", json={
        "dieta": "onívoro",
        "habitat_especifico": "floresta"
    })

    assert res.status_code == 200

    data = res.get_json()
    assert data["dieta"] == "onívoro"
    assert data["habitat_especifico"] == "floresta"

    # =========================
    # VERIFY UPDATE (GET REAL)
    # =========================
    res = client.get(f"/animais/{animal_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["dieta"] == "onívoro"
    assert data["habitat_especifico"] == "floresta"

    # =========================
    # DELETE
    # =========================
    res = client.delete(f"/animais/{animal_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["id"] == animal_id

    # =========================
    # VERIFY DELETE
    # =========================
    res = client.get(f"/animais/{animal_id}")
    assert res.status_code == 404