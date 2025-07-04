from flask import jsonify
from flask import flash, request, Blueprint, current_app
from agenda_contatos.logger_singleton import Logger


categoria_bp = Blueprint('categoria_bp', __name__)
logger = Logger.get_instance()

#rota para buscar todas categorias
@categoria_bp.route('/categorias', methods=['GET'])
def listar_todas():
    from agenda_contatos.Model.categoria import listar_categorias
    logger.info("Listando todas as categorias")
    categorias = listar_categorias()
    if categorias is False or categorias is None:
        return jsonify([]), 200
    if hasattr(categorias, 'get_data'):
        return categorias
    return jsonify(categorias), 200

#rota para buscar uma categoria pelo id
@categoria_bp.route('/categoria/<int:id>', methods=['GET'])
def listar_uma(id):
    from agenda_contatos.Model.categoria import listar_categoria
    logger.info(f"Listando categoria com id: {id}")
    categoria = listar_categoria(id)
    if categoria is False or categoria is None:
        return jsonify(None), 200
    if hasattr(categoria, 'get_data'):
        return categoria
    return jsonify(categoria), 200

#rota para criar uma nova categoria
@categoria_bp.route('/categoria', methods=['POST'])
def criar_categoria():
    from agenda_contatos.Model.categoria import novo_categoria
    logger.info("Criando uma nova categoria")
    try:
        data = request.get_json()
        categoria = data['categoria']
    except Exception as e:
        logger.error(f"Dados inválidos: {e}")
        return jsonify({'status': 'Falha', 'error': 'Dados inválidos'}), 400

    if novo_categoria(categoria):
        logger.info("Categoria criada com sucesso")
        return jsonify({'status': 'ok'}), 201
    else:
        logger.error("Falha ao criar categoria")
        return jsonify({'status': 'Falha'}), 500


#rota para atualizar uma categoria
@categoria_bp.route('/categoria/<int:id>', methods=['PUT'])
def atualizar_categoria(id):
    from agenda_contatos.Model.categoria import editar_categoria
    logger.info(f"Atualizando categoria com id: {id}")
    try:
        data = request.get_json()
        categoria = data['categoria']
    except Exception as e:
        logger.error(f"Dados inválidos: {e}")
        return jsonify({'status': 'Falha', 'error': 'Dados inválidos'}), 400

    if editar_categoria(id, categoria):
        logger.info("Categoria atualizada com sucesso")
        return jsonify({'status': 'ok'}), 200
    else:
        logger.error("Falha ao atualizar categoria")
        return jsonify({'status': 'Falha'}), 500
    
#rota para deletar um contato
@categoria_bp.route('/categoria/<int:id>', methods=['DELETE'])
def deletar_categoria_route(id):
    from agenda_contatos.Model.categoria import deletar_categoria
    logger.info(f"Deletando categoria com id: {id}")
    if deletar_categoria(id):
        logger.info("Categoria deletada com sucesso")
        return jsonify({'status': 'ok'}), 200
    else:
        logger.error("Falha ao deletar categoria")
        return jsonify({'status': 'Falha'}), 500