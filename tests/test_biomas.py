
from main import app

client = app.test_client()


def test_criar_bioma():

    response = client.post("/biomas", data={
        "nome": "Caatinga",
        "descricao": "Bioma brasileiro"
    })

    print(response.data.decode())

    assert response.status_code == 200