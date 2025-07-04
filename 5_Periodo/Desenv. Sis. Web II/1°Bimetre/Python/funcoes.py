import jwt
from flask import jsonify
from flask import request, current_app

def valida_token():
    try:
        #valida token
        
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):
            return jsonify({"message": "Token não fornecido"}), 401
           
        dados = jwt.decode(token.split(" ")[1], current_app.config.get("SECRET_KEY"), algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expirado"}), 401