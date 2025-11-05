from app.controllers.usuario_controller import usuario_bp
from flask import Flask, render_template, redirect, session, url_for
from config import FLASK

def create_app():
    app = Flask(__name__)

    app.secret_key = FLASK["secret_key"]

    app.register_blueprint(usuario_bp, url_prefix="/usuario")

    @app.route("/")
    def home():
        if (not "id" in session):
            return redirect(url_for("usuario.login"))
        
        return render_template("index.html")

    return app