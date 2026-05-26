from flask import Flask, request
from backend.database import Base, engine

# IMPORTA TODOS OS MODELS
from backend.models.usuario import Usuario
from backend.models.animal import Animal
from backend.models.bioma import Bioma

from backend.controller.usuario_controller import (
    cadastrar_usuario,
    atualizar_usuario,
    deletar_usuario,
    listar_usuarios,
    buscar_usuario
)
from backend.controller.animal_controller import (
    cadastrar_animal,
    atualizar_animal,
    deletar_animal,
    listar_animais,
    buscar_animal
)

from backend.controller.bioma_controller import (
    cadastrar_bioma,
    atualizar_bioma,
    deletar_bioma,
    listar_biomas,
    buscar_bioma,
)


app = Flask(__name__)

# CRIA AS TABELAS
Base.metadata.create_all(bind=engine)


@app.route("/")
def home():
    return "Aplicação rodando com sucesso!"

#---------------------- Usuários ----------------------
@app.route("/usuarios", methods=["POST"])
def rota_cadastrar_usuario():
    dados_formulario = request.form.to_dict()
    resultado = cadastrar_usuario(dados_formulario)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"


@app.route("/usuarios", methods=["GET"])
def rota_listar_usuarios():
    return listar_usuarios()


@app.route("/usuarios/<int:usuario_id>", methods=["GET"])
def rota_buscar_usuario(usuario_id):
    return buscar_usuario(usuario_id)


@app.route("/usuarios/<int:usuario_id>", methods=["POST"])
def rota_atualizar_usuario(usuario_id):
    dados_formulario = request.form.to_dict()
    resultado = atualizar_usuario(usuario_id,dados_formulario)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"


@app.route("/usuarios/<int:usuario_id>/deletar", methods=["POST"])
def rota_deletar_usuario(usuario_id):
    resultado = deletar_usuario(usuario_id)
    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"



#---------------------- Animais ----------------------
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

@app.route("/animais", methods=["GET"])
def rota_listar_animais():
    return listar_animais()


@app.route("/animais/<int:animal_id>", methods=["GET"])
def rota_buscar_animal(animal_id):
    return buscar_animal(animal_id)

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

