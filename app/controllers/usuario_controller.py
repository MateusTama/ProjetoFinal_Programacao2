from flask import Blueprint, request, render_template, session, redirect, url_for, flash 
from app.models.usuario import Usuario
from app.dao.usuario_dao import UsuarioDAO 
from app.utils.password_utils import gerar_hash_senha, checar_hash_senha

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route("/login", methods=["GET", "POST"])
def login():
    # Se o usuário já estiver logado
    if ("id" in session):
        return redirect(url_for("home"))
    
    # Caso seja uma tentativa de login
    if (request.method == "POST"):
        email = request.form["email"]
        senha = request.form["senha"]

        usuario_dao = UsuarioDAO()
        usuario = usuario_dao.buscar_por_email(email)

        # Checa se o email corresponde a um usuário já cadastrado no sistema
        if (not usuario):
            flash("Usuário não cadastrado", "error")
            return render_template("login.html")
        
        # Checa se a senha corresponde ao hash armazenado no banco de dados
        if (not checar_hash_senha(usuario.senha, senha)):
            flash("A senha está incorreta", "error")
            return render_template("login.html")

        # Armazena o id do usuário logado na sessão
        session["id"] = usuario.id
        return redirect(url_for("home"))
    
    return render_template("login.html")

@usuario_bp.route("/cadastrar", methods=["GET","POST"])
def cadastrar():
    # Se for um usuário que já está logado
    if ("id" in session):
        return redirect(url_for("home"))
    
    if (request.method == "POST"):
        primeiro_nome = request.form["primeiro_nome"]
        sobrenome = request.form["sobrenome"]
        email = request.form["email"]
        senha = request.form["senha"]
        senha_hash = gerar_hash_senha(senha)

        usuario_dao = UsuarioDAO()
        usuario = Usuario(primeiro_nome=primeiro_nome, sobrenome=sobrenome, email=email, senha=senha_hash)
        
        usuario_dao.inserir(usuario)
        
        return redirect(url_for("usuario.login"))

    return render_template("cadastro_usuario.html")