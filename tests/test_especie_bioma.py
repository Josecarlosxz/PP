def test_especie_bioma_crud(client):
    # =========================
    # CREATE DEPENDENCIES
    # =========================

    esp = client.post("/especies/", json={
        "nome_popular": "Onça",
        "nome_cientifico": "Panthera onca",
        "descricao": "Felino",
        "tipo": "especie",
        "usuario_id": 1
    }).get_json()["id"]

    bio = client.post("/biomas/", json={
        "nome": "Pantanal",
        "descricao": "Área alagada",
        "clima": "úmido",
        "vegetacao": "mista"
    }).get_json()["id"]

    # =========================
    # CREATE RELATION
    # =========================
    res = client.post("/especie-bioma/", json={
        "especie_id": esp,
        "bioma_id": bio
    })

    assert res.status_code == 200

    data = res.get_json()
    assert data is not None
    assert "id" in data

    rel_id = data["id"]

    assert data["especie_id"] == esp
    assert data["bioma_id"] == bio

    # =========================
    # READ
    # =========================
    res = client.get(f"/especie-bioma/{rel_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["id"] == rel_id
    assert data["especie_id"] == esp
    assert data["bioma_id"] == bio

    # =========================
    # DELETE
    # =========================
    res = client.delete(f"/especie-bioma/{rel_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["id"] == rel_id

    # =========================
    # VERIFY DELETE
    # =========================
    res = client.get(f"/especie-bioma/{rel_id}")
    assert res.status_code == 404