from flask import Blueprint, render_template


frontend_bp = Blueprint(
    "frontend",
    __name__
)


# ============================================================
# INDEX
# ============================================================

@frontend_bp.route("/")
def index():

    return render_template("index.html")


# ============================================================
# LOGIN
# ============================================================

@frontend_bp.route("/login")
def login_page():

    return render_template("login.html")


# ============================================================
# CADASTRO
# ============================================================

@frontend_bp.route("/cadastro")
def cadastro_page():

    return render_template("cadastro.html")


# ============================================================
# HOME
# ============================================================

@frontend_bp.route("/home")
def home():

    return render_template("home.html")