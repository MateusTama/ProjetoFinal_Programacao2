from werkzeug.security import generate_password_hash, check_password_hash

def gerar_hash_senha(senha):
    return generate_password_hash(senha)

def checar_hash_senha(senha_hash, senha):
    return check_password_hash(senha_hash, senha)