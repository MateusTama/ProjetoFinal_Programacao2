from db import get_connection
from app.models.usuario import Usuario

class UsuarioDAO:
    def inserir(self, usuario:Usuario):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO usuario
            (primeiro_nome, sobrenome, email, senha)
            VALUES
            (%s, %s, %s, %s)
        """, (usuario.primeiro_nome, usuario.sobrenome, usuario.email, usuario.senha))

        connection.commit()

        cursor.close()
        connection.close()

    def buscar_por_email(self, email):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, primeiro_nome, sobrenome, email, senha
            FROM usuario
            WHERE 
            email = %s
        """, (email,))

        registro_usuario = cursor.fetchone()

        cursor.close()
        connection.close()

        if registro_usuario:
            id = registro_usuario[0]
            primeiro_nome = registro_usuario[1]
            sobrenome = registro_usuario[2]
            # email = registro_usuario[3] igual ao parâmetro email
            senha_hash = registro_usuario[4]
            return Usuario(id, primeiro_nome, sobrenome, email, senha_hash)
        
        return None
