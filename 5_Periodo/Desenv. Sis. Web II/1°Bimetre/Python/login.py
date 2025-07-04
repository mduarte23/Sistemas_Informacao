import pymysql
import jwt
import datetime
from db_config import connect_db
from flask import jsonify
from flask import flash, request, Blueprint, current_app

login_bp = Blueprint('login', __name__)

#busca todos usuarios
@login_bp.route('/login', methods=['POST'])
def login():
    try:
        usuario = request.json
        email = usuario['email']
        senha = usuario['senha']

        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM usuario WHERE email=%s AND senha=%s", (email, senha))
        rows = cursor.fetchall()

        if len(rows) == 0:
            resp = {"sucess": False}, 401
        else:
            global SECRET_KEY
            token = jwt.encode({"user": email, 
                                #data de expiraçao do token = 1 hora
                                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, 
                                current_app.config.get("SECRET_KEY"), 
                                algorithm="HS256")
            resp = {"sucess": True, "token": token}, 200


        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
