

from backend.controller.token_controller import gerar_token

def test_gerar_token():

    resultado = gerar_token(1)

    print(resultado)

    assert resultado is not None
    