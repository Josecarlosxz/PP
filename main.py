from flask import Flask, request

from backend.controller.animal_controller import (
    cadastrar_animal,
    atualizar_animal,
    deletar_animal,
)
from backend.controller.bioma_controller import (
    cadastrar_bioma,
    atualizar_bioma,
    deletar_bioma,
    listar_biomas,
    buscar_bioma,
)

app = Flask(__name__)


@app.route("/animais", methods=["POST"])
def rota_cadastrar_animal():
    dados_formulario = request.form.to_dict()
    resultado = cadastrar_animal(dados_formulario)
    return f"Sucesso: {resultado['mensagem']}"


@app.route("/animais/<int:animal_id>", methods=["POST"])
def rota_atualizar_animal(animal_id):
    dados_formulario = request.form.to_dict()
    resultado = atualizar_animal(animal_id, dados_formulario)
    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"
    return f"Sucesso: {resultado['mensagem']}"


@app.route("/animais/<int:animal_id>/deletar", methods=["POST"])
def rota_deletar_animal(animal_id):
    resultado = deletar_animal(animal_id)
    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"
    return f"Sucesso: {resultado['mensagem']}"


# ---------------------- Biomas ----------------------

@app.route("/biomas", methods=["POST"])
def rota_cadastrar_bioma():
    dados_formulario = request.form.to_dict()
    resultado = cadastrar_bioma(dados_formulario)
    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"
    return f"Sucesso: {resultado['mensagem']}"


@app.route("/biomas/<int:bioma_id>", methods=["POST"])
def rota_atualizar_bioma(bioma_id: int):
    dados_formulario = request.form.to_dict()
    resultado = atualizar_bioma(bioma_id, dados_formulario)
    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"
    return f"Sucesso: {resultado['mensagem']}"


@app.route("/biomas/<int:bioma_id>/deletar", methods=["POST"])
def rota_deletar_bioma(bioma_id: int):
    resultado = deletar_bioma(bioma_id)
    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"
    return f"Sucesso: {resultado['mensagem']}"


@app.route("/biomas", methods=["GET"])
def rota_listar_biomas():
    return listar_biomas()


@app.route("/biomas/<int:bioma_id>", methods=["GET"])
def rota_buscar_bioma(bioma_id: int):
    return buscar_bioma(bioma_id)


if __name__ == "__main__":
    app.run(debug=True)

