
import os

from flask import Flask, render_template
from dotenv import load_dotenv
from backend.utils.auth import login_required

load_dotenv()


# ============================================================
# IMPORT DOS CONTROLLERS
# ============================================================

from backend.controllers.usuario_controller import usuario_bp
from backend.controllers.login_controller import login_bp
from backend.controllers.logout_controller import logout_bp

from backend.controllers.especie_controller import especie_bp
from backend.controllers.animal_controller import animal_bp
from backend.controllers.planta_controller import planta_bp
from backend.controllers.bioma_controller import bioma_bp
from backend.controllers.especie_bioma_controller import especie_bioma_bp
from backend.controllers.token_controller import token_bp
from backend.controllers.participante_controller import participante_bp


# ============================================================
# FACTORY APP
# ============================================================

def create_app():

    app = Flask(
        __name__,
        template_folder="frontend/templates",
        static_folder="frontend/static"
    )

    # ========================================================
    # CONFIGURAÇÕES
    # ========================================================

    app.config["JSON_SORT_KEYS"] = False

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    if not app.config["SECRET_KEY"]:
        raise RuntimeError(
            "SECRET_KEY não configurada no arquivo .env"
        )

    # ========================================================
    # FRONTEND
    # ========================================================

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")


    @app.route("/login", methods=["GET"])
    def login_page():
        return render_template("login.html")


    @app.route("/cadastro", methods=["GET"])
    def cadastro_page():
        return render_template("cadastro.html")


    @app.route("/home", methods=["GET"])
    def home_page():
        return render_template("home.html")


    # ========================================================
    # API
    # ========================================================

    app.register_blueprint(usuario_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(logout_bp)

    app.register_blueprint(especie_bp)
    app.register_blueprint(animal_bp)
    app.register_blueprint(planta_bp)
    app.register_blueprint(bioma_bp)
    app.register_blueprint(especie_bioma_bp)
    app.register_blueprint(token_bp)
    app.register_blueprint(participante_bp)

    return app


# ============================================================
# CRIAÇÃO DA APLICAÇÃO
# ============================================================

app = create_app()


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )

