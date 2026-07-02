def test_bioma_crud(client):
    # =========================
    # CREATE
    # =========================
    res = client.post("/biomas/", json={
        "nome": "Amazônia",
        "descricao": "Floresta tropical",
        "clima": "quente",
        "vegetacao": "densa"
    })

    assert res.status_code == 200

    data = res.get_json()
    assert data is not None
    assert "id" in data

    bioma_id = data["id"]

    assert data["nome"] == "Amazônia"
    assert data["clima"] == "quente"
    assert data["vegetacao"] == "densa"

    # =========================
    # READ
    # =========================
    res = client.get(f"/biomas/{bioma_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["id"] == bioma_id
    assert data["nome"] == "Amazônia"
    assert data["descricao"] == "Floresta tropical"
    assert data["clima"] == "quente"
    assert data["vegetacao"] == "densa"

    # =========================
    # UPDATE
    # =========================
    res = client.put(f"/biomas/{bioma_id}", json={
        "nome": "Amazônia Atualizada",
        "descricao": "Floresta atualizada",
        "clima": "úmido",
        "vegetacao": "muito densa"
    })

    assert res.status_code == 200

    data = res.get_json()
    assert data["nome"] == "Amazônia Atualizada"
    assert data["clima"] == "úmido"
    assert data["vegetacao"] == "muito densa"

    # =========================
    # VERIFY UPDATE (GET REAL)
    # =========================
    res = client.get(f"/biomas/{bioma_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["nome"] == "Amazônia Atualizada"
    assert data["clima"] == "úmido"
    assert data["vegetacao"] == "muito densa"

    # =========================
    # DELETE
    # =========================
    res = client.delete(f"/biomas/{bioma_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["id"] == bioma_id

    # =========================
    # VERIFY DELETE
    # =========================
    res = client.get(f"/biomas/{bioma_id}")
    assert res.status_code == 404