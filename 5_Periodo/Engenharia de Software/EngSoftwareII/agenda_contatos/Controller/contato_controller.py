from flask import jsonify
from flask import flash, request, Blueprint, current_app
from agenda_contatos.logger_singleton import Logger

contato_bp = Blueprint('contato_bp', __name__)
logger = Logger.get_instance()

#rota para buscar todos os contatos
@contato_bp.route('/contatos', methods=['GET'])
def listar_todos():
    from agenda_contatos.Model.contato import listar_contatos
    logger.info("Listando todos os contatos")
    contatos = listar_contatos()
    if contatos is False or contatos is None:
        return jsonify([]), 200
    if hasattr(contatos, 'get_data'):
        # Se já for um Response Flask
        return contatos
    return jsonify(contatos), 200

#rota para buscar um contato pelo id
@contato_bp.route('/contato/<int:id>', methods=['GET'])
def listar_um(id):
    from agenda_contatos.Model.contato import listar_contato
    logger.info(f"Listando contato com id: {id}")
    contato = listar_contato(id)
    if contato is False or contato is None:
        return jsonify(None), 200
    if hasattr(contato, 'get_data'):
        return contato
    return jsonify(contato), 200

#rota para criar um novo contato
@contato_bp.route('/contato', methods=['POST'])
def criar_contato():
    from agenda_contatos.Model.contato import novo_contato
    logger.info("Criando um novo contato")
    try:
        data = request.get_json()
        nome = data['nome']
        telefone = data['telefone']
        email = data['email']
        categoria = data['categoria']
    except Exception as e:
        logger.error(f"Dados inválidos: {e}")
        return jsonify({'status': 'fail', 'error': 'Dados inválidos'}), 400

    if novo_contato(nome, telefone, email, categoria):
        logger.info("Contato criado com sucesso")
        return jsonify({'status': 'ok'}), 201
    else:
        logger.error("Falha ao criar contato")
        return jsonify({'status': 'fail'}), 500

#rota para atualizar um contato
@contato_bp.route('/contato/<int:id>', methods=['PUT'])
def atualizar_contato(id):
    from agenda_contatos.Model.contato import alterar_contato
    logger.info(f"Atualizando contato com id: {id}")
    try:
        data = request.get_json()
        nome = data['nome']
        telefone = data['telefone']
        email = data['email']
        categoria = data['categoria']
    except Exception as e:
        logger.error(f"Dados inválidos: {e}")
        return jsonify({'status': 'fail', 'error': 'Dados inválidos'}), 400

    if alterar_contato(id, nome, telefone, email, categoria):
        logger.info("Contato atualizado com sucesso")
        return jsonify({'status': 'ok'}), 200
    else:
        logger.error("Falha ao atualizar contato")
        return jsonify({'status': 'fail'}), 500
    
#rota para deletar um contato
@contato_bp.route('/contato/<int:id>', methods=['DELETE'])
def apagar_contato(id):
    from agenda_contatos.Model.contato import deletar_contato
    logger.info(f"Deletando contato com id: {id}")
    if deletar_contato(id):
        logger.info("Contato deletado com sucesso")
        return jsonify({'status': 'ok'}), 200
    else:
        logger.error("Falha ao deletar contato")
        return jsonify({'status': 'fail'}), 500