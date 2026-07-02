def test_usuario_crud(client):
    # =========================
    # CREATE
    # =========================
    res = client.post("/usuarios/", json={
        "nome": "Kaik",
        "email": "kaik@email.com",
        "senha": "123"
    })

    assert res.status_code == 200

    data = res.get_json()
    assert data is not None
    assert "id" in data

    usuario_id = data["id"]

    # valida CREATE de verdade
    assert data["nome"] == "Kaik"
    assert data["email"] == "kaik@email.com"

    # =========================
    # READ
    # =========================
    res = client.get(f"/usuarios/{usuario_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["id"] == usuario_id
    assert data["email"] == "kaik@email.com"

    # =========================
    # UPDATE
    # =========================
    res = client.put(f"/usuarios/{usuario_id}", json={
        "nome": "Kaik Atualizado"
    })

    assert res.status_code == 200

    # valida UPDATE persistido
    res = client.get(f"/usuarios/{usuario_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["nome"] == "Kaik Atualizado"

    # =========================
    # DELETE
    # =========================
    res = client.delete(f"/usuarios/{usuario_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["id"] == usuario_id

    # =========================
    # VERIFY DELETE
    # =========================
    res = client.get(f"/usuarios/{usuario_id}")
    assert res.status_code == 404