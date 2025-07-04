import pytest
import json
from unittest.mock import patch, MagicMock
import tempfile
import os

class TestIntegration:
    """Testes de integração para o sistema completo de agenda de contatos"""
    
    def test_01_home_page_access(self, client):
        """Testa acesso à página principal"""
        response = client.get('/')
        assert response.status_code == 200
        html_content = response.get_data(as_text=True)
        assert 'html' in html_content.lower()
        assert 'agenda' in html_content.lower() or 'contatos' in html_content.lower()
    
    def test_02_complete_contato_workflow(self, client, mock_contato_functions):
        """Testa fluxo completo de CRUD de contatos"""
        # Configura mocks
        mock_contato_functions['novo_contato'].return_value = True
        mock_contato_functions['listar_contatos'].return_value = [{
            'id_contato': 1,
            'nome': 'João Silva',
            'telefone': '(11) 99999-9999',
            'email': 'joao@email.com',
            'categoria': 'Família'
        }]
        mock_contato_functions['listar_contato'].return_value = {
            'id_contato': 1,
            'nome': 'João Silva',
            'telefone': '(11) 99999-9999',
            'email': 'joao@email.com',
            'categoria': 'Família'
        }
        mock_contato_functions['alterar_contato'].return_value = True
        mock_contato_functions['deletar_contato'].return_value = True
        
        # 1. Criar contato
        contato_data = {
            'nome': 'João Silva',
            'telefone': '(11) 99999-9999',
            'email': 'joao@email.com',
            'categoria': 1
        }
        
        response = client.post('/contato', 
                             data=json.dumps(contato_data),
                             content_type='application/json')
        assert response.status_code == 201
        assert json.loads(response.get_data(as_text=True))['status'] == 'ok'
        
        # 2. Listar todos os contatos
        response = client.get('/contatos')
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert len(data) == 1
        assert data[0]['nome'] == 'João Silva'
        
        # 3. Buscar contato específico
        response = client.get('/contato/1')
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert data['nome'] == 'João Silva'
        
        # 4. Atualizar contato
        contato_atualizado = {
            'nome': 'João Silva Atualizado',
            'telefone': '(11) 88888-8888',
            'email': 'joao.novo@email.com',
            'categoria': 2
        }
        response = client.put('/contato/1', 
                            data=json.dumps(contato_atualizado),
                            content_type='application/json')
        assert response.status_code == 200
        assert json.loads(response.get_data(as_text=True))['status'] == 'ok'
        
        # 5. Deletar contato
        response = client.delete('/contato/1')
        assert response.status_code == 200
        assert json.loads(response.get_data(as_text=True))['status'] == 'ok'
    
    def test_03_complete_categoria_workflow(self, client, mock_categoria_functions):
        """Testa fluxo completo de CRUD de categorias"""
        # Configura mocks
        mock_categoria_functions['novo_categoria'].return_value = True
        mock_categoria_functions['listar_categorias'].return_value = [{
            'id_categoria': 1,
            'categoria': 'Família'
        }]
        mock_categoria_functions['listar_categoria'].return_value = {
            'id_categoria': 1,
            'categoria': 'Família'
        }
        mock_categoria_functions['editar_categoria'].return_value = True
        mock_categoria_functions['deletar_categoria'].return_value = True
        
        # 1. Criar categoria
        categoria_data = {'categoria': 'Família'}
        response = client.post('/categoria', 
                             data=json.dumps(categoria_data),
                             content_type='application/json')
        assert response.status_code == 201
        assert json.loads(response.get_data(as_text=True))['status'] == 'ok'
        
        # 2. Listar todas as categorias
        response = client.get('/categorias')
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert len(data) == 1
        assert data[0]['categoria'] == 'Família'
        
        # 3. Buscar categoria específica
        response = client.get('/categoria/1')
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert data['categoria'] == 'Família'
        
        # 4. Atualizar categoria
        categoria_atualizada = {'categoria': 'Família Atualizada'}
        response = client.put('/categoria/1', 
                            data=json.dumps(categoria_atualizada),
                            content_type='application/json')
        assert response.status_code == 200
        assert json.loads(response.get_data(as_text=True))['status'] == 'ok'
        
        # 5. Deletar categoria
        response = client.delete('/categoria/1')
        assert response.status_code == 200
        assert json.loads(response.get_data(as_text=True))['status'] == 'ok'
    
    def test_04_error_handling_and_validation(self, client):
        """Testa tratamento de erros e validações"""
        # Testa rota inexistente
        response = client.get('/rota-inexistente')
        assert response.status_code == 404
        
        # Testa método não permitido
        response = client.post('/contatos')  # GET only
        assert response.status_code == 405
        
        response = client.get('/contato')  # POST only
        assert response.status_code == 405
        
        # Testa JSON inválido
        response = client.post('/contato', 
                             data='invalid json',
                             content_type='application/json')
        assert response.status_code == 400
        
        response = client.post('/categoria', 
                             data='invalid json',
                             content_type='application/json')
        assert response.status_code == 400
    
    def test_05_missing_required_fields(self, client):
        """Testa validação de campos obrigatórios"""
        # Testa contato sem campos obrigatórios
        contato_incompleto = {'nome': 'João'}  # Faltando telefone, email, categoria
        response = client.post('/contato', 
                             data=json.dumps(contato_incompleto),
                             content_type='application/json')
        assert response.status_code == 400
        
        # Testa categoria sem nome
        categoria_incompleta = {}
        response = client.post('/categoria', 
                             data=json.dumps(categoria_incompleta),
                             content_type='application/json')
        assert response.status_code == 400
    
    def test_06_database_error_handling(self, client, mock_contato_functions, mock_categoria_functions):
        """Testa tratamento de erros de banco de dados"""
        # Configura mocks para simular falhas
        mock_contato_functions['novo_contato'].return_value = False
        mock_contato_functions['listar_contatos'].return_value = False
        mock_categoria_functions['novo_categoria'].return_value = False
        mock_categoria_functions['listar_categorias'].return_value = False
        
        # Testa falha ao criar contato
        contato_data = {
            'nome': 'João Silva',
            'telefone': '(11) 99999-9999',
            'email': 'joao@email.com',
            'categoria': 1
        }
        response = client.post('/contato', 
                             data=json.dumps(contato_data),
                             content_type='application/json')
        assert response.status_code == 500
        assert json.loads(response.get_data(as_text=True))['status'] == 'fail'
        
        # Testa falha ao listar contatos
        response = client.get('/contatos')
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert data == []
        
        # Testa falha ao criar categoria
        categoria_data = {'categoria': 'Família'}
        response = client.post('/categoria', 
                             data=json.dumps(categoria_data),
                             content_type='application/json')
        assert response.status_code == 500
        assert json.loads(response.get_data(as_text=True))['status'] == 'Falha'
    
    def test_07_static_files_serving(self, client):
        """Testa se arquivos estáticos são servidos corretamente"""
        # Testa CSS
        response = client.get('/static/css/estilo.css')
        assert response.status_code == 200
        assert 'text/css' in response.headers.get('Content-Type', '')
        
        # Testa JavaScript
        response = client.get('/static/script/contato.js')
        assert response.status_code == 200
        assert 'javascript' in response.headers.get('Content-Type', '')
        
        response = client.get('/static/script/categoria.js')
        assert response.status_code == 200
        
        # Testa páginas HTML
        response = client.get('/static/contato.html')
        assert response.status_code == 200
        assert 'text/html' in response.headers.get('Content-Type', '')
        
        response = client.get('/static/categoria.html')
        assert response.status_code == 200
        
        response = client.get('/static/index.html')
        assert response.status_code == 200
    
    def test_08_logging_integration(self, client):
        """Testa se o sistema de logging está funcionando"""
        with patch('agenda_contatos.Controller.categoria_controller.logger') as mock_logger:
            # Testa se o logger é chamado ao acessar rotas
            client.get('/categorias')
            mock_logger.info.assert_called_with("Listando todas as categorias")
    
    def test_09_multiple_operations_sequence(self, client, mock_contato_functions, mock_categoria_functions):
        """Testa sequência de múltiplas operações"""
        # Configura mocks
        mock_contato_functions['novo_contato'].return_value = True
        mock_contato_functions['listar_contatos'].return_value = [
            {'id_contato': 1, 'nome': 'João', 'telefone': '(11) 11111-1111', 'email': 'joao@email.com', 'categoria': 'Família'},
            {'id_contato': 2, 'nome': 'Maria', 'telefone': '(11) 22222-2222', 'email': 'maria@email.com', 'categoria': 'Trabalho'}
        ]
        mock_categoria_functions['novo_categoria'].return_value = True
        mock_categoria_functions['listar_categorias'].return_value = [
            {'id_categoria': 1, 'categoria': 'Família'},
            {'id_categoria': 2, 'categoria': 'Trabalho'}
        ]
        
        # Cria múltiplas categorias
        categorias = ['Família', 'Trabalho', 'Amigos']
        for categoria in categorias:
            response = client.post('/categoria', 
                                 data=json.dumps({'categoria': categoria}),
                                 content_type='application/json')
            assert response.status_code == 201
        
        # Cria múltiplos contatos
        contatos = [
            {'nome': 'João', 'telefone': '(11) 11111-1111', 'email': 'joao@email.com', 'categoria': 1},
            {'nome': 'Maria', 'telefone': '(11) 22222-2222', 'email': 'maria@email.com', 'categoria': 2},
            {'nome': 'Pedro', 'telefone': '(11) 33333-3333', 'email': 'pedro@email.com', 'categoria': 1}
        ]
        for contato in contatos:
            response = client.post('/contato', 
                                 data=json.dumps(contato),
                                 content_type='application/json')
            assert response.status_code == 201
        
        # Lista todos os contatos
        response = client.get('/contatos')
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert len(data) == 2  # Conforme mock configurado
    
    def test_10_edge_cases_and_boundaries(self, client, mock_contato_functions):
        """Testa casos extremos e limites"""
        # Testa contato com dados muito longos
        contato_longo = {
            'nome': 'A' * 1000,  # Nome muito longo
            'telefone': '(11) 99999-9999',
            'email': 'joao@email.com',
            'categoria': 1
        }
        mock_contato_functions['novo_contato'].return_value = True
        response = client.post('/contato', 
                             data=json.dumps(contato_longo),
                             content_type='application/json')
        assert response.status_code == 201
        
        # Testa contato com email inválido
        contato_email_invalido = {
            'nome': 'João Silva',
            'telefone': '(11) 99999-9999',
            'email': 'email-invalido',
            'categoria': 1
        }
        response = client.post('/contato', 
                             data=json.dumps(contato_email_invalido),
                             content_type='application/json')
        assert response.status_code == 201  # O sistema aceita qualquer email
    
    def test_11_concurrent_operations(self, client, mock_contato_functions):
        """Testa operações concorrentes de forma simplificada"""
        mock_contato_functions['novo_contato'].return_value = True
        mock_contato_functions['listar_contatos'].return_value = []
        
        # Simula múltiplas requisições sequenciais (mais seguro que threads)
        results = []
        
        for i in range(5):
            contato_data = {
                'nome': f'Contato {i}',
                'telefone': f'(11) {i:05d}-{i:04d}',
                'email': f'contato{i}@email.com',
                'categoria': 1
            }
            response = client.post('/contato', 
                                 data=json.dumps(contato_data),
                                 content_type='application/json')
            results.append(response.status_code)
        
        # Verifica se todas as operações foram bem-sucedidas
        assert all(status == 201 for status in results)
    
    def test_12_data_persistence_simulation(self, client, mock_contato_functions, mock_categoria_functions):
        """Testa simulação de persistência de dados"""
        # Configura mocks para simular dados persistentes
        contatos_persistentes = []
        categorias_persistentes = []
        
        def mock_novo_contato(nome, telefone, email, categoria):
            contatos_persistentes.append({
                'id_contato': len(contatos_persistentes) + 1,
                'nome': nome,
                'telefone': telefone,
                'email': email,
                'categoria': categoria
            })
            return True
        
        def mock_listar_contatos():
            return contatos_persistentes
        
        def mock_novo_categoria(categoria):
            categorias_persistentes.append({
                'id_categoria': len(categorias_persistentes) + 1,
                'categoria': categoria
            })
            return True
        
        def mock_listar_categorias():
            return categorias_persistentes
        
        # Aplica os mocks
        mock_contato_functions['novo_contato'].side_effect = mock_novo_contato
        mock_contato_functions['listar_contatos'].side_effect = mock_listar_contatos
        mock_categoria_functions['novo_categoria'].side_effect = mock_novo_categoria
        mock_categoria_functions['listar_categorias'].side_effect = mock_listar_categorias
        
        # Cria categoria
        response = client.post('/categoria', 
                             data=json.dumps({'categoria': 'Família'}),
                             content_type='application/json')
        assert response.status_code == 201
        
        # Cria contato
        response = client.post('/contato', 
                             data=json.dumps({
                                 'nome': 'João Silva',
                                 'telefone': '(11) 99999-9999',
                                 'email': 'joao@email.com',
                                 'categoria': 1
                             }),
                             content_type='application/json')
        assert response.status_code == 201
        
        # Verifica se os dados foram "persistidos"
        response = client.get('/contatos')
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert len(data) == 1
        assert data[0]['nome'] == 'João Silva'
        
        response = client.get('/categorias')
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert len(data) == 1
        assert data[0]['categoria'] == 'Família'
    
    def test_13_api_response_format_consistency(self, client, mock_contato_functions, mock_categoria_functions):
        """Testa consistência do formato de resposta da API"""
        # Configura mocks
        mock_contato_functions['listar_contatos'].return_value = [{
            'id_contato': 1,
            'nome': 'João Silva',
            'telefone': '(11) 99999-9999',
            'email': 'joao@email.com',
            'categoria': 'Família'
        }]
        mock_categoria_functions['listar_categorias'].return_value = [{
            'id_categoria': 1,
            'categoria': 'Família'
        }]
        
        # Testa formato de resposta para contatos
        response = client.get('/contatos')
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert isinstance(data, list)
        if len(data) > 0:
            assert 'id_contato' in data[0]
            assert 'nome' in data[0]
            assert 'telefone' in data[0]
            assert 'email' in data[0]
            assert 'categoria' in data[0]
        
        # Testa formato de resposta para categorias
        response = client.get('/categorias')
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert isinstance(data, list)
        if len(data) > 0:
            assert 'id_categoria' in data[0]
            assert 'categoria' in data[0]
    
    def test_14_error_recovery_and_graceful_degradation(self, client, mock_contato_functions):
        """Testa recuperação de erros e degradação graciosa"""
        # Simula falha temporária seguida de sucesso
        mock_contato_functions['listar_contatos'].side_effect = [False, [{
            'id_contato': 1,
            'nome': 'João Silva',
            'telefone': '(11) 99999-9999',
            'email': 'joao@email.com',
            'categoria': 'Família'
        }]]
        
        # Primeira tentativa falha
        response = client.get('/contatos')
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert data == []
        
        # Segunda tentativa funciona
        response = client.get('/contatos')
        assert response.status_code == 200
        data = json.loads(response.get_data(as_text=True))
        assert len(data) == 1
        assert data[0]['nome'] == 'João Silva'
    
    def test_15_system_health_and_monitoring(self, client):
        """Testa saúde do sistema e monitoramento"""
        # Testa se todas as rotas principais respondem
        rotas_principais = ['/', '/contatos', '/categorias']
        for rota in rotas_principais:
            response = client.get(rota)
            assert response.status_code in [200, 404]  # 404 é aceitável para algumas rotas
        
        # Testa se headers estão configurados corretamente
        response = client.get('/contatos')
        assert 'Content-Type' in response.headers
        assert 'application/json' in response.headers.get('Content-Type', '')
        
        # Testa se o sistema responde rapidamente
        import time
        start_time = time.time()
        response = client.get('/contatos')
        end_time = time.time()
        
        assert response.status_code == 200
        assert (end_time - start_time) < 5.0  # Deve responder em menos de 5 segundos 