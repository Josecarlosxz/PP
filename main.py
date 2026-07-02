from flask import Flask, request, session
from backend.database import Base, engine


# ---------------- TOKENS ----------------
from backend.controller.token_controller import gerar_token
import backend.models

from backend.controller.token_controller import (
    gerar_token,
    entrar
)

# ---------------- MODELS ----------------
from backend.models.usuario import Usuario
from backend.models.bioma import Bioma
from backend.models.especie import Especie
from backend.models.animal import Animal
from backend.models.planta import Planta

# ---------------- CONTROLLERS ----------------
from backend.controller.usuario_controller import (
    cadastrar_usuario,
    atualizar_usuario,
    deletar_usuario,
    listar_usuarios,
    buscar_usuario
)

from backend.controller.bioma_controller import (
    cadastrar_bioma,
    atualizar_bioma,
    deletar_bioma,
    listar_biomas,
    buscar_bioma,
)

from backend.controller.especie_controller import (
    cadastrar_especie,
    atualizar_especie,
    deletar_especie,
    listar_especies,
    buscar_especie
)

from backend.controller.animal_controller import (
    cadastrar_animal,
    atualizar_animal,
    deletar_animal,
    listar_animais,
    buscar_animal
)

from backend.controller.planta_controller import (
    cadastrar_planta,
    atualizar_planta,
    deletar_planta,
    listar_plantas,
    buscar_planta
)


app = Flask(__name__)
import backend.models
# CRIA AS TABELAS
Base.metadata.create_all(bind=engine)

app.secret_key = "chave_mais_que_secreta"

@app.route("/")
def home():
    return "Aplicação rodando com sucesso!"


# ======================
# USUÁRIOS
# ======================
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
    resultado = atualizar_usuario(usuario_id, dados_formulario)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"


@app.route("/usuarios/<int:usuario_id>/deletar", methods=["POST"])
def rota_deletar_usuario(usuario_id):
    resultado = deletar_usuario(usuario_id)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"


# ======================
# BIOMAS
# ======================
@app.route("/biomas", methods=["POST"])
def rota_cadastrar_bioma():
    dados_formulario = request.form.to_dict()
    resultado = cadastrar_bioma(dados_formulario)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"


@app.route("/biomas", methods=["GET"])
def rota_listar_biomas():
    return listar_biomas()


@app.route("/biomas/<int:bioma_id>", methods=["GET"])
def rota_buscar_bioma(bioma_id):
    return buscar_bioma(bioma_id)


@app.route("/biomas/<int:bioma_id>", methods=["POST"])
def rota_atualizar_bioma(bioma_id):
    dados_formulario = request.form.to_dict()
    resultado = atualizar_bioma(bioma_id, dados_formulario)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"


@app.route("/biomas/<int:bioma_id>/deletar", methods=["POST"])
def rota_deletar_bioma(bioma_id):
    resultado = deletar_bioma(bioma_id)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"


# ======================
# ESPÉCIES
# ======================
@app.route("/especies", methods=["POST"])
def rota_cadastrar_especie():
    dados_formulario = request.form.to_dict()
    resultado = cadastrar_especie(dados_formulario)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"


@app.route("/especies", methods=["GET"])
def rota_listar_especies():
    return listar_especies()


@app.route("/especies/<int:especie_id>", methods=["GET"])
def rota_buscar_especie(especie_id):
    return buscar_especie(especie_id)


@app.route("/especies/<int:especie_id>", methods=["POST"])
def rota_atualizar_especie(especie_id):
    dados_formulario = request.form.to_dict()
    resultado = atualizar_especie(especie_id, dados_formulario)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"


@app.route("/especies/<int:especie_id>/deletar", methods=["POST"])
def rota_deletar_especie(especie_id):
    resultado = deletar_especie(especie_id)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"


# ======================
# ANIMAIS
# ======================
@app.route("/animais", methods=["POST"])
def rota_cadastrar_animal():
    dados_formulario = request.form.to_dict()
    resultado = cadastrar_animal(dados_formulario)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"


@app.route("/animais", methods=["GET"])
def rota_listar_animais():
    return listar_animais()


@app.route("/animais/<int:animal_id>", methods=["GET"])
def rota_buscar_animal(animal_id):
    return buscar_animal(animal_id)


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


# ======================
# PLANTAS
# ======================
@app.route("/plantas", methods=["POST"])
def rota_cadastrar_planta():
    dados_formulario = request.form.to_dict()
    resultado = cadastrar_planta(dados_formulario)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"


@app.route("/plantas", methods=["GET"])
def rota_listar_plantas():
    return listar_plantas()


@app.route("/plantas/<int:planta_id>", methods=["GET"])
def rota_buscar_planta(planta_id):
    return buscar_planta(planta_id)


@app.route("/plantas/<int:planta_id>", methods=["POST"])
def rota_atualizar_planta(planta_id):
    dados_formulario = request.form.to_dict()
    resultado = atualizar_planta(planta_id, dados_formulario)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"


@app.route("/plantas/<int:planta_id>/deletar", methods=["POST"])
def rota_deletar_planta(planta_id):
    resultado = deletar_planta(planta_id)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"Sucesso: {resultado['mensagem']}"


# ======================
# TOKEN
# ======================
@app.route("/gerar-token/<int:professor_id>", methods=["POST"])
def rota_gerar_token(professor_id):

    resultado = gerar_token(professor_id)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    return f"""
    Token gerado com sucesso!<br>
    Código: {resultado['codigo']}
    """

@app.route("/entrar", methods=["POST"])
def rota_entrar():

    dados_formulario = request.form.to_dict()

    resultado = entrar(dados_formulario)

    if "erro" in resultado:
        return f"Erro: {resultado['erro']}"

    session["participante_id"] = resultado["participante_id"]
    session["nome"] = resultado["nome"]
    session["token_id"] = resultado["token_id"]

    return f"Sucesso: {resultado['mensagem']}"

if __name__ == "__main__":
    app.run(debug=True)