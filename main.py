from flask import Flask

# =========================
# IMPORT DOS CONTROLLERS
# =========================
from backend.controllers.usuario_controller import usuario_bp
from backend.controllers.especie_controller import especie_bp
from backend.controllers.animal_controller import animal_bp
from backend.controllers.planta_controller import planta_bp
from backend.controllers.bioma_controller import bioma_bp
from backend.controllers.especie_bioma_controller import especie_bioma_bp
from backend.controllers.token_controller import token_bp
from backend.controllers.participante_controller import participante_bp


# =========================
# FACTORY APP (BOA PRÁTICA)
# =========================
def create_app():
    app = Flask(__name__)

    # =========================
    # CONFIGURAÇÕES (opcional)
    # =========================
    app.config["JSON_SORT_KEYS"] = False

    # =========================
    # REGISTRO DE BLUEPRINTS
    # =========================
    app.register_blueprint(usuario_bp)
    app.register_blueprint(especie_bp)
    app.register_blueprint(animal_bp)
    app.register_blueprint(planta_bp)
    app.register_blueprint(bioma_bp)
    app.register_blueprint(especie_bioma_bp)
    app.register_blueprint(token_bp)
    app.register_blueprint(participante_bp)

    return app


# =========================
# EXECUÇÃO DO SERVIDOR
# =========================
app = create_app()

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )