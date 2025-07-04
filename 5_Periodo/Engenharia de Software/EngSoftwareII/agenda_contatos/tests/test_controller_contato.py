import pytest
import json
from unittest.mock import patch

class TestContatoController:
    """Testes para o controlador de contato"""
    
    def test_listar_todos_contatos_success(self, client, sample_contatos_list):
        """Testa listagem de todos os contatos com sucesso"""
        with patch('agenda_contatos.Model.contato.listar_contatos') as mock_listar:
            mock_listar.return_value = sample_contatos_list
            response = client.get('/contatos')
            assert response.status_code == 200
            data = json.loads(response.get_data(as_text=True))
            assert len(data) == 2
            assert data[0]['nome'] == 'João Silva'
            mock_listar.assert_called_once()
    
    def test_criar_contato_success(self, client, sample_contato_data):
        """Testa criação de contato com sucesso"""
        with patch('agenda_contatos.Model.contato.novo_contato') as mock_novo:
            mock_novo.return_value = True
            response = client.post('/contato', 
                                 data=json.dumps(sample_contato_data),
                                 content_type='application/json')
            assert response.status_code == 201
            data = json.loads(response.get_data(as_text=True))
            assert data['status'] == 'ok'
            mock_novo.assert_called_once_with(
                'João Silva', 
                '(11) 99999-9999', 
                'joao@email.com', 
                1
            )
    
    def test_criar_contato_missing_data(self, client):
        """Testa criação de contato com dados faltando"""
        incomplete_data = {
            'nome': 'João Silva',
            'telefone': '(11) 99999-9999'
        }
        response = client.post('/contato', 
                             data=json.dumps(incomplete_data),
                             content_type='application/json')
        assert response.status_code == 400
    
    def test_atualizar_contato_success(self, client, sample_contato_data):
        """Testa atualização de contato com sucesso"""
        with patch('agenda_contatos.Model.contato.alterar_contato') as mock_alterar:
            mock_alterar.return_value = True
            response = client.put('/contato/1', 
                                data=json.dumps(sample_contato_data),
                                content_type='application/json')
            assert response.status_code == 200
            data = json.loads(response.get_data(as_text=True))
            assert data['status'] == 'ok'
            mock_alterar.assert_called_once_with(
                1, 'João Silva', '(11) 99999-9999', 'joao@email.com', 1
            )
    
    def test_apagar_contato_success(self, client):
        """Testa deleção de contato com sucesso"""
        with patch('agenda_contatos.Model.contato.deletar_contato') as mock_deletar:
            mock_deletar.return_value = True
            response = client.delete('/contato/1')
            assert response.status_code == 200
            data = json.loads(response.get_data(as_text=True))
            assert data['status'] == 'ok'
            mock_deletar.assert_called_once_with(1)

    def test_criar_contato_dados_json_invalidos(self, client):
        """Testa criação de contato com dados JSON inválidos"""
        with patch('agenda_contatos.Model.contato.novo_contato') as mock_novo:
            # Simula request sem dados JSON
            response = client.post('/contato', 
                                 data='dados_invalidos',
                                 content_type='text/plain')
            
            assert response.status_code == 400
            assert response.get_json()['status'] == 'fail'
            assert response.get_json()['error'] == 'Dados inválidos'
            mock_novo.assert_not_called()

    def test_atualizar_contato_dados_json_invalidos(self, client):
        """Testa atualização de contato com dados JSON inválidos"""
        with patch('agenda_contatos.Model.contato.alterar_contato') as mock_alterar:
            # Simula request sem dados JSON
            response = client.put('/contato/1', 
                                data='dados_invalidos',
                                content_type='text/plain')
            
            assert response.status_code == 400
            assert response.get_json()['status'] == 'fail'
            assert response.get_json()['error'] == 'Dados inválidos'
            mock_alterar.assert_not_called()

    def test_criar_contato_dados_incompletos(self, client):
        """Testa criação de contato com dados incompletos"""
        with patch('agenda_contatos.Model.contato.novo_contato') as mock_novo:
            # Simula dados incompletos (faltando email)
            dados_incompletos = {
                'nome': 'João Silva',
                'telefone': '11987654321',
                'categoria': 'Trabalho'
                # email está faltando
            }
            
            response = client.post('/contato', 
                                 json=dados_incompletos)
            
            assert response.status_code == 400
            assert response.get_json()['status'] == 'fail'
            assert response.get_json()['error'] == 'Dados inválidos'
            mock_novo.assert_not_called()

    def test_atualizar_contato_dados_incompletos(self, client):
        """Testa atualização de contato com dados incompletos"""
        with patch('agenda_contatos.Model.contato.alterar_contato') as mock_alterar:
            # Simula dados incompletos (faltando telefone)
            dados_incompletos = {
                'nome': 'João Silva',
                'email': 'joao@email.com',
                'categoria': 'Trabalho'
                # telefone está faltando
            }
            
            response = client.put('/contato/1', 
                                json=dados_incompletos)
            
            assert response.status_code == 400
            assert response.get_json()['status'] == 'fail'
            assert response.get_json()['error'] == 'Dados inválidos'
            mock_alterar.assert_not_called()

    def test_inserir_e_apagar_contato(self, client):
        """Testa inserir um contato e depois apagar o mesmo contato"""
        dados_contato = {
            'nome': 'João Silva',
            'telefone': '11987654321',
            'email': 'joao@email.com',
            'categoria': 'Trabalho'
        }
        
        with patch('agenda_contatos.Model.contato.novo_contato') as mock_novo, \
             patch('agenda_contatos.Model.contato.deletar_contato') as mock_deletar:
            
            # Configura os mocks
            mock_novo.return_value = True
            mock_deletar.return_value = True
            
            # Primeiro, insere o contato
            response_insert = client.post('/contato', json=dados_contato)
            assert response_insert.status_code == 201
            assert response_insert.get_json()['status'] == 'ok'
            mock_novo.assert_called_once_with(
                dados_contato['nome'],
                dados_contato['telefone'],
                dados_contato['email'],
                dados_contato['categoria']
            )
            
            # Depois, apaga o contato que foi inserido
            # Simula que o contato inserido tem ID 1
            response_delete = client.delete('/contato/1')
            assert response_delete.status_code == 200
            assert response_delete.get_json()['status'] == 'ok'
            mock_deletar.assert_called_once_with(1)
            
            # Verifica que ambas as operações foram chamadas
            assert mock_novo.call_count == 1
            assert mock_deletar.call_count == 1 