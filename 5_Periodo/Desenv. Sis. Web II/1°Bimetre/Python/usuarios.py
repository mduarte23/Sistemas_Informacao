import pymysql
import jwt
from db_config import connect_db
from flask import jsonify
from flask import flash, request, Blueprint, current_app
from funcoes import valida_token

usuario_bp = Blueprint('usuario_bp', __name__)

#busca todos usuarios
@usuario_bp.route('/usuarios')
def usuario():
    valida_token()
            
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM usuario")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@usuario_bp.route('/usuario/<id>')
def usuario_id(id):
    valida_token()
      
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM usuario WHERE idusuario=%s", (id))
        row = cursor.fetchall()
        resp = jsonify(row[0])
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@usuario_bp.route('/usuario', methods=['POST'])
def usuarionovo():
    valida_token()
      
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        #pega os dados do JSON
        usuario = request.json
        nome = usuario['nome']
        email = usuario['email']
        telefone = usuario['telefone']

        #insere no banco
        cursor.execute("INSERT INTO usuario (nome, email, telefone) VALUES (%s, %s, %s)", (nome, email, telefone))
        conn.commit()
        resp = jsonify({"message" : 'Usuario criado com sucesso!'})
        resp.status_code = 200
        return resp
    
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    

@usuario_bp.route('/usuario/<id>', methods=['PUT'])
def usuarioalterar(id):
    valida_token()
      
    try:
        
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        #pega os dados do JSON
        usuario = request.json
        nome = usuario['nome']
        email = usuario['email']
        telefone = usuario['telefone']

        #atualiza no banco
        cursor.execute("UPDATE usuario SET nome=%s, email=%s, telefone=%s WHERE idusuario=%s", (nome, email, telefone, id))
        conn.commit()
        resp = jsonify({"message" : 'Usuario atualizado com sucesso!'})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

@usuario_bp.route('/usuario/<id>', methods=['DELETE'])
def usuarioexcluir(id):
    valida_token()
      
    try:
        
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("DELETE FROM usuario WHERE idusuario=%s", (id))
        conn.commit()
        resp = jsonify({"message" : 'Usuario deletado com sucesso!'})
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

