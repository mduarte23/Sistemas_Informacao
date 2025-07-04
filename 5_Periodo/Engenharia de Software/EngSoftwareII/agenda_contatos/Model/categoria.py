import pymysql
import pymysql.cursors
from agenda_contatos.Model.conexao import DatabaseConnection
from flask import jsonify
from agenda_contatos.database import Conexao


def novo_categoria(categoria):
    try:
        #abre a conexao com BD
        conexao = DatabaseConnection().get_connection()
        cursor = conexao.cursor(pymysql.cursors.DictCursor)
        #comando para SQL
        sql = "INSERT INTO categoria (categoria) VALUES (%s)"
        cursor.execute(sql, (categoria))
        conexao.commit()
        
        #retorna ok
        return True
    except Exception as e:
        #retorna falha
        return False 
    finally:  
        #fecha a conexao com o BD
        cursor.close()
        

def listar_categorias():
    try:
        #abre a conexao com BD
        conexao = DatabaseConnection().get_connection()
        cursor = conexao.cursor(pymysql.cursors.DictCursor)
        #comando para SQL
        sql = "SELECT * FROM categoria ORDER BY id_categoria"
        cursor.execute(sql)
        #retorna os contatos
        return jsonify(cursor.fetchall())
    except Exception as e:
        #retorna falha
        return False
    finally:
        #fecha a conexao com o BD
        try:
            cursor.close()
        except Exception:
            pass


def listar_categoria(id):
    try:
        #abre a conexao com BD
        conexao = DatabaseConnection().get_connection()
        cursor = conexao.cursor(pymysql.cursors.DictCursor)
        #comando para SQL
        sql = "SELECT * FROM categoria WHERE id_categoria = %s"
        cursor.execute(sql, (id))

        #retorna o contato
        return jsonify(cursor.fetchone())
    except Exception as e:
        #retorna falha
        return False    
    finally:  
        #fecha a conexao com o BD
        cursor.close()
        

def editar_categoria(id, categoria):
    try:
        #abre a conexao com BD
        conexao = DatabaseConnection().get_connection()
        cursor = conexao.cursor(pymysql.cursors.DictCursor)
        #comando para SQL
        sql = "UPDATE categoria SET categoria = %s WHERE id_categoria = %s"
        cursor.execute(sql, (categoria, id))
        conexao.commit()
        #retorna ok
        return True
    except Exception as e:
        #retorna falha
        return False
    finally:
        #fecha a conexao com o BD
        cursor.close()
        

def deletar_categoria(id):
    try:
        #abre a conexao com BD
        conexao = DatabaseConnection().get_connection()
        cursor = conexao.cursor(pymysql.cursors.DictCursor)
        #comando para SQL
        sql = "DELETE FROM categoria WHERE id_categoria = %s"
        cursor.execute(sql, (id))
        conexao.commit()
        #retorna ok
        return True
    except Exception as e:
        #retorna falha
        return False
    finally:
        #fecha a conexao com o BD
        cursor.close()
        

