import pytest
import json
from unittest.mock import patch

class TestCategoriaController:
    """Testes para o controlador de categoria"""
    
    def test_listar_todas_categorias_success(self, client, sample_categorias_list):
        """Testa listagem de todas as categorias com sucesso"""
        with patch('agenda_contatos.Model.categoria.listar_categorias') as mock_listar:
            mock_listar.return_value = sample_categorias_list
            response = client.get('/categorias')
            assert response.status_code == 200
            data = json.loads(response.get_data(as_text=True))
            assert len(data) == 2
            assert data[0]['categoria'] == 'Família'
            mock_listar.assert_called_once()
    
    def test_criar_categoria_success(self, client, sample_categoria_data):
        """Testa criação de categoria com sucesso"""
        with patch('agenda_contatos.Model.categoria.novo_categoria') as mock_novo:
            mock_novo.return_value = True
            response = client.post('/categoria', 
                                 data=json.dumps(sample_categoria_data),
                                 content_type='application/json')
            assert response.status_code == 201
            data = json.loads(response.get_data(as_text=True))
            assert data['status'] == 'ok'
            mock_novo.assert_called_once_with('Família')
    
    def test_criar_categoria_missing_data(self, client):
        """Testa criação de categoria com dados faltando"""
        incomplete_data = {}
        response = client.post('/categoria', 
                             data=json.dumps(incomplete_data),
                             content_type='application/json')
        assert response.status_code == 400
    
    def test_atualizar_categoria_success(self, client, sample_categoria_data):
        """Testa atualização de categoria com sucesso"""
        with patch('agenda_contatos.Model.categoria.editar_categoria') as mock_editar:
            mock_editar.return_value = True
            response = client.put('/categoria/1', 
                                data=json.dumps(sample_categoria_data),
                                content_type='application/json')
            assert response.status_code == 200
            data = json.loads(response.get_data(as_text=True))
            assert data['status'] == 'ok'
            mock_editar.assert_called_once_with(1, 'Família')
    
    def test_deletar_categoria_success(self, client):
        """Testa deleção de categoria com sucesso"""
        with patch('agenda_contatos.Model.categoria.deletar_categoria') as mock_deletar:
            mock_deletar.return_value = True
            response = client.delete('/categoria/1')
            assert response.status_code == 200
            data = json.loads(response.get_data(as_text=True))
            assert data['status'] == 'ok'
            mock_deletar.assert_called_once_with(1)

    def test_criar_categoria_dados_json_invalidos(self, client):
        """Testa criação de categoria com dados JSON inválidos"""
        with patch('agenda_contatos.Model.categoria.novo_categoria') as mock_nova:
            # Simula request sem dados JSON
            response = client.post('/categoria', 
                                 data='dados_invalidos',
                                 content_type='text/plain')
            
            assert response.status_code == 400
            assert response.get_json()['status'] == 'Falha'
            assert response.get_json()['error'] == 'Dados inválidos'
            mock_nova.assert_not_called()

    def test_atualizar_categoria_dados_json_invalidos(self, client):
        """Testa atualização de categoria com dados JSON inválidos"""
        with patch('agenda_contatos.Model.categoria.editar_categoria') as mock_alterar:
            # Simula request sem dados JSON
            response = client.put('/categoria/1', 
                                data='dados_invalidos',
                                content_type='text/plain')
            
            assert response.status_code == 400
            assert response.get_json()['status'] == 'Falha'
            assert response.get_json()['error'] == 'Dados inválidos'
            mock_alterar.assert_not_called()

    def test_criar_categoria_dados_incompletos(self, client):
        """Testa criação de categoria com dados incompletos"""
        with patch('agenda_contatos.Model.categoria.novo_categoria') as mock_nova:
            # Simula dados incompletos (faltando categoria)
            dados_incompletos = {
                'nome': 'Trabalho'
                # categoria está faltando
            }
            
            response = client.post('/categoria', 
                                 json=dados_incompletos)
            
            assert response.status_code == 400
            assert response.get_json()['status'] == 'Falha'
            assert response.get_json()['error'] == 'Dados inválidos'
            mock_nova.assert_not_called()

    def test_atualizar_categoria_dados_incompletos(self, client):
        """Testa atualização de categoria com dados incompletos"""
        with patch('agenda_contatos.Model.categoria.editar_categoria') as mock_alterar:
            # Simula dados incompletos (faltando categoria)
            dados_incompletos = {
                'nome': 'Trabalho'
                # categoria está faltando
            }
            
            response = client.put('/categoria/1', 
                                json=dados_incompletos)
            
            assert response.status_code == 400
            assert response.get_json()['status'] == 'Falha'
            assert response.get_json()['error'] == 'Dados inválidos'
            mock_alterar.assert_not_called()

    def test_inserir_e_apagar_categoria(self, client):
        """Testa inserir uma categoria e depois apagar a mesma categoria"""
        nome_categoria = 'TesteCategoria'
        
        with patch('agenda_contatos.Model.categoria.novo_categoria') as mock_novo, \
             patch('agenda_contatos.Model.categoria.deletar_categoria') as mock_deletar:
            
            # Configura os mocks
            mock_novo.return_value = True
            mock_deletar.return_value = True
            
            # Primeiro, insere a categoria
            response_insert = client.post('/categoria', json={'categoria': nome_categoria})
            assert response_insert.status_code == 201
            assert response_insert.get_json()['status'] == 'ok'
            mock_novo.assert_called_once_with(nome_categoria)
            
            # Depois, apaga a categoria que foi inserida
            # Simula que a categoria inserida tem ID 1
            response_delete = client.delete('/categoria/1')
            assert response_delete.status_code == 200
            assert response_delete.get_json()['status'] == 'ok'
            mock_deletar.assert_called_once_with(1)
            
            # Verifica que ambas as operações foram chamadas
            assert mock_novo.call_count == 1
            assert mock_deletar.call_count == 1 