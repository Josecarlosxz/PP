def test_planta_crud(client):
    # =========================
    # CREATE
    # =========================
    res = client.post("/plantas/", json={
        "nome_popular": "Rosa",
        "nome_cientifico": "Rosa sp",
        "descricao": "Planta ornamental",
        "usuario_id": 1,
        "tipo_folha": "simples",
        "medicinal": True
    })

    assert res.status_code == 200

    data = res.get_json()
    assert data is not None
    assert "id" in data

    planta_id = data["id"]

    assert data["nome_popular"] == "Rosa"
    assert data["nome_cientifico"] == "Rosa sp"
    assert data["descricao"] == "Planta ornamental"
    assert data["tipo_folha"] == "simples"
    assert data["medicinal"] is True

    # =========================
    # READ
    # =========================
    res = client.get(f"/plantas/{planta_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["id"] == planta_id
    assert data["nome_popular"] == "Rosa"

    # =========================
    # UPDATE
    # =========================
    res = client.put(f"/plantas/{planta_id}", json={
        "medicinal": False
    })

    assert res.status_code == 200

    # =========================
    # VERIFY UPDATE
    # =========================
    res = client.get(f"/plantas/{planta_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["medicinal"] is False

    # =========================
    # DELETE
    # =========================
    res = client.delete(f"/plantas/{planta_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["id"] == planta_id

    # =========================
    # VERIFY DELETE
    # =========================
    res = client.get(f"/plantas/{planta_id}")
    assert res.status_code == 404