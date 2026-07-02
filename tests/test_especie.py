def test_especie_crud(client):
    # =========================
    # CREATE
    # =========================
    res = client.post("/especies/", json={
        "nome_popular": "Onça",
        "nome_cientifico": "Panthera onca",
        "descricao": "Felino",
        "tipo": "especie",
        "usuario_id": 1
    })

    assert res.status_code == 200

    data = res.get_json()
    assert data is not None
    assert "id" in data

    especie_id = data["id"]

    assert data["nome_popular"] == "Onça"
    assert data["nome_cientifico"] == "Panthera onca"
    assert data["descricao"] == "Felino"
    assert data["tipo"] == "especie"
    assert data["usuario_id"] == 1

    # =========================
    # READ
    # =========================
    res = client.get(f"/especies/{especie_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["id"] == especie_id
    assert data["nome_popular"] == "Onça"
    assert data["descricao"] == "Felino"

    # =========================
    # UPDATE
    # =========================
    res = client.put(f"/especies/{especie_id}", json={
        "descricao": "Atualizado"
    })

    assert res.status_code == 200

    data = res.get_json()
    assert data["descricao"] == "Atualizado"

    # =========================
    # VERIFY UPDATE (GET REAL)
    # =========================
    res = client.get(f"/especies/{especie_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["descricao"] == "Atualizado"

    # =========================
    # DELETE
    # =========================
    res = client.delete(f"/especies/{especie_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["id"] == especie_id

    # =========================
    # VERIFY DELETE
    # =========================
    res = client.get(f"/especies/{especie_id}")
    assert res.status_code == 404