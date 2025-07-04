import pytest
import sys
import os
from unittest.mock import Mock, patch

# Adiciona o diretório pai ao path para importar os módulos do projeto
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agenda_contatos.server import app
from logger_singleton import Logger

@pytest.fixture
def client():
    """Fixture para criar um cliente de teste Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@pytest.fixture
def mock_db_connection():
    """Fixture para mockar a conexão com o banco de dados"""
    with patch('Model.conexao.DatabaseConnection') as mock_db:
        mock_connection = Mock()
        mock_cursor = Mock()
        mock_db.return_value.get_connection.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        yield mock_db, mock_connection, mock_cursor

@pytest.fixture
def sample_contato_data():
    """Dados de exemplo para um contato"""
    return {
        'nome': 'João Silva',
        'telefone': '(11) 99999-9999',
        'email': 'joao@email.com',
        'categoria': 1
    }

@pytest.fixture
def sample_categoria_data():
    """Dados de exemplo para uma categoria"""
    return {
        'categoria': 'Família'
    }

@pytest.fixture
def sample_contatos_list():
    """Lista de contatos de exemplo"""
    return [
        {
            'id_contato': 1,
            'nome': 'João Silva',
            'telefone': '(11) 99999-9999',
            'email': 'joao@email.com',
            'categoria': 'Família'
        },
        {
            'id_contato': 2,
            'nome': 'Maria Santos',
            'telefone': '(11) 88888-8888',
            'email': 'maria@email.com',
            'categoria': 'Trabalho'
        }
    ]

@pytest.fixture
def sample_categorias_list():
    """Lista de categorias de exemplo"""
    return [
        {
            'id_categoria': 1,
            'categoria': 'Família'
        },
        {
            'id_categoria': 2,
            'categoria': 'Trabalho'
        }
    ]

@pytest.fixture(autouse=True)
def reset_logger():
    """Reset do logger antes de cada teste"""
    Logger._instance = None

@pytest.fixture
def mock_contato_functions():
    """Mock para todas as funções do modelo de contato"""
    with patch('agenda_contatos.Model.contato.novo_contato') as mock_novo, \
         patch('agenda_contatos.Model.contato.listar_contatos') as mock_listar, \
         patch('agenda_contatos.Model.contato.listar_contato') as mock_listar_um, \
         patch('agenda_contatos.Model.contato.alterar_contato') as mock_alterar, \
         patch('agenda_contatos.Model.contato.deletar_contato') as mock_deletar:
        yield {
            'novo_contato': mock_novo,
            'listar_contatos': mock_listar,
            'listar_contato': mock_listar_um,
            'alterar_contato': mock_alterar,
            'deletar_contato': mock_deletar
        }

@pytest.fixture
def mock_categoria_functions():
    """Mock para todas as funções do modelo de categoria"""
    with patch('agenda_contatos.Model.categoria.novo_categoria') as mock_novo, \
         patch('agenda_contatos.Model.categoria.listar_categorias') as mock_listar, \
         patch('agenda_contatos.Model.categoria.listar_categoria') as mock_listar_uma, \
         patch('agenda_contatos.Model.categoria.editar_categoria') as mock_editar, \
         patch('agenda_contatos.Model.categoria.deletar_categoria') as mock_deletar:
        yield {
            'novo_categoria': mock_novo,
            'listar_categorias': mock_listar,
            'listar_categoria': mock_listar_uma,
            'editar_categoria': mock_editar,
            'deletar_categoria': mock_deletar
        } 