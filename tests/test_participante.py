def test_participante_crud(client):
    # =========================
    # CREATE
    # =========================
    res = client.post("/participantes/", json={
        "nome": "João",
        "token_id": 1
    })

    assert res.status_code == 200

    data = res.get_json()
    assert data is not None
    assert "id" in data

    part_id = data["id"]

    # validações do CREATE (somente se seu controller retornar isso)
    assert data["nome"] == "João"

    # =========================
    # READ
    # =========================
    res = client.get(f"/participantes/{part_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["id"] == part_id

    # =========================
    # DELETE
    # =========================
    res = client.delete(f"/participantes/{part_id}")
    assert res.status_code == 200

    data = res.get_json()
    assert data["id"] == part_id

    # =========================
    # VERIFY DELETE
    # =========================
    res = client.get(f"/participantes/{part_id}")
    assert res.status_code == 404