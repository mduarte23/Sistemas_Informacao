import pymysql
import pymysql.cursors
from agenda_contatos.Model.conexao import DatabaseConnection
from flask import jsonify

def novo_contato(nome, telefone, email, id_categoria):
    try:
        conexao = DatabaseConnection().get_connection()
        cursor = conexao.cursor(pymysql.cursors.DictCursor)
        #comando para SQL
        sql = "INSERT INTO contato (nome, telefone, email, id_categoria) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, telefone, email, id_categoria))
        conexao.commit()
        
        #retorna ok
        return True
    except Exception as e:
        #retorna falha
        return False 
    finally:  
        #fecha a conexao com o BD
        cursor.close()
        
        
def listar_contatos():
    try:
        #abre a conexao com BD
        conexao = DatabaseConnection().get_connection()
        cursor = conexao.cursor(pymysql.cursors.DictCursor)
        #comando para SQL
        sql = "SELECT c.id_contato, c.nome, c.telefone, c.email, cat.categoria FROM contato c INNER JOIN categoria cat ON c.id_categoria = cat.id_categoria ORDER BY id_contato"
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
        

def listar_contato(id):
    try:
        #abre a conexao com BD
        conexao = DatabaseConnection().get_connection()
        cursor = conexao.cursor(pymysql.cursors.DictCursor)
        #comando para SQL
        sql = "SELECT c.id_contato, c.nome, c.telefone, c.email, cat.categoria FROM contato c INNER JOIN categoria cat ON c.id_categoria = cat.id_categoria WHERE id_contato = %s"
        cursor.execute(sql, (id))

        #retorna o contato
        return jsonify(cursor.fetchone())
    except Exception as e:
        #retorna falha
        return False    
    finally:  
        #fecha a conexao com o BD
        cursor.close()
        

def alterar_contato(id, nome, telefone, email, categoria):
    try:
        #abre a conexao com BD
        conexao = DatabaseConnection().get_connection()
        cursor = conexao.cursor(pymysql.cursors.DictCursor)
        #comando para SQL
        sql = "UPDATE contato SET nome = %s, telefone = %s, email = %s, id_categoria = %s WHERE id_contato = %s"
        cursor.execute(sql, (nome, telefone, email, categoria, id))
        conexao.commit()
        
        #retorna ok
        return True
    except Exception as e:
        #retorna falha
        return False 
    finally:  
        #fecha a conexao com o BD
        cursor.close()
        

def deletar_contato(id):
    try:
        #abre a conexao com BD
        conexao = DatabaseConnection().get_connection()
        cursor = conexao.cursor(pymysql.cursors.DictCursor)
        #comando para SQL
        sql = "DELETE FROM contato WHERE id_contato = %s"
        cursor.execute(sql, (id))
        conexao.commit()
        return True
    except Exception as e:
        #retorna falha
        return False
    finally:
        #fecha a conexao com o BD
        cursor.close()
        

