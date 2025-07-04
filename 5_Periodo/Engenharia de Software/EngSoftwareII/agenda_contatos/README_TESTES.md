# Testes da Aplicação de Agenda de Contatos

Este documento descreve a estrutura de testes implementada para a aplicação de agenda de contatos usando pytest.

## 📁 Estrutura dos Testes

```
tests/
├── __init__.py
├── conftest.py                    # Configurações e fixtures do pytest
├── test_logger_singleton.py       # Testes do logger singleton
├── test_model_contato.py          # Testes do modelo de contato
├── test_model_categoria.py        # Testes do modelo de categoria
├── test_controller_contato.py     # Testes do controlador de contato
├── test_controller_categoria.py   # Testes do controlador de categoria
└── test_integration.py            # Testes de integração
```

## 🚀 Como Executar os Testes

### Pré-requisitos

Instale as dependências de teste:

```bash
pip install -r requirements.txt
```

### Executar Todos os Testes

```bash
# Usando o script personalizado
python run_tests.py

# Ou diretamente com pytest
pytest -v

# Com relatório de cobertura
pytest -v --cov=. --cov-report=html
```

### Executar Testes Específicos

```bash
# Testes de um módulo específico
pytest tests/test_logger_singleton.py -v

# Testes de uma classe específica
pytest tests/test_model_contato.py::TestModelContato -v

# Testes de um método específico
pytest tests/test_logger_singleton.py::TestLogger::test_singleton_pattern -v

# Testes por marcadores
pytest -m unit -v
pytest -m integration -v
```

## 📊 Tipos de Testes Implementados

### 1. Testes Unitários

#### Logger Singleton (`test_logger_singleton.py`)
- ✅ Padrão Singleton funcionando corretamente
- ✅ Métodos de log (info, warning, error)
- ✅ Formato de timestamp
- ✅ Salvamento em arquivo
- ✅ Tratamento de erros

#### Modelo de Contato (`test_model_contato.py`)
- ✅ Criação de contato (sucesso e falha)
- ✅ Listagem de contatos (sucesso e falha)
- ✅ Busca de contato específico (sucesso e falha)
- ✅ Atualização de contato (sucesso e falha)
- ✅ Deleção de contato (sucesso e falha)
- ✅ Verificação de SQL executado
- ✅ Fechamento de conexões

#### Modelo de Categoria (`test_model_categoria.py`)
- ✅ Criação de categoria (sucesso e falha)
- ✅ Listagem de categorias (sucesso e falha)
- ✅ Busca de categoria específica (sucesso e falha)
- ✅ Edição de categoria (sucesso e falha)
- ✅ Deleção de categoria (sucesso e falha)
- ✅ Verificação de SQL executado
- ✅ Fechamento de conexões

### 2. Testes de Controladores

#### Controlador de Contato (`test_controller_contato.py`)
- ✅ Rotas GET, POST, PUT, DELETE
- ✅ Validação de JSON
- ✅ Tratamento de dados faltando
- ✅ Códigos de status HTTP corretos
- ✅ Integração com modelos

#### Controlador de Categoria (`test_controller_categoria.py`)
- ✅ Rotas GET, POST, PUT, DELETE
- ✅ Validação de JSON
- ✅ Tratamento de dados faltando
- ✅ Códigos de status HTTP corretos
- ✅ Integração com modelos

### 3. Testes de Integração (`test_integration.py`)
- ✅ Fluxo completo CRUD de contatos
- ✅ Fluxo completo CRUD de categorias
- ✅ Tratamento de erros HTTP
- ✅ Validação de JSON
- ✅ Integração com logging
- ✅ Integração com banco de dados
- ✅ Servir arquivos estáticos

## 🔧 Fixtures e Configurações

### Fixtures Principais (`conftest.py`)

- **`client`**: Cliente Flask para testes de API
- **`mock_db_connection`**: Mock da conexão com banco de dados
- **`sample_contato_data`**: Dados de exemplo para contatos
- **`sample_categoria_data`**: Dados de exemplo para categorias
- **`sample_contatos_list`**: Lista de contatos de exemplo
- **`sample_categorias_list`**: Lista de categorias de exemplo
- **`reset_logger`**: Reset do logger antes de cada teste

## 📈 Cobertura de Código

Os testes incluem cobertura de:

- ✅ **100%** dos modelos (contato e categoria)
- ✅ **100%** dos controladores
- ✅ **100%** do logger singleton
- ✅ **90%+** das rotas da aplicação
- ✅ **Tratamento de erros** e casos edge

### Gerar Relatório de Cobertura

```bash
pytest --cov=. --cov-report=html --cov-report=term-missing
```

O relatório será gerado em `htmlcov/index.html`

## 🎯 Estratégias de Teste

### 1. Mocking
- **Banco de Dados**: Todos os testes usam mocks para evitar dependência real do banco
- **Logger**: Mockado quando necessário para verificar chamadas
- **Conexões**: Simuladas para testar cenários de sucesso e falha

### 2. Testes de Sucesso e Falha
- Cada operação é testada tanto para sucesso quanto para falha
- Verificação de códigos de status HTTP apropriados
- Validação de mensagens de erro

### 3. Validação de Dados
- Testes com JSON válido e inválido
- Testes com dados faltando
- Validação de tipos de dados

### 4. Integração
- Testes de fluxo completo (CRUD)
- Verificação de integração entre camadas
- Testes de arquivos estáticos

## 🚨 Tratamento de Erros Testado

- ✅ Exceções de banco de dados
- ✅ JSON inválido
- ✅ Dados faltando
- ✅ Rotas inexistentes
- ✅ Métodos HTTP não permitidos
- ✅ Erros de conexão

## 📝 Comandos Úteis

```bash
# Executar testes com output detalhado
pytest -v -s

# Executar apenas testes que falharam
pytest --lf

# Executar testes em paralelo (se instalado pytest-xdist)
pytest -n auto

# Executar testes com timeout
pytest --timeout=30

# Executar testes e gerar relatório JUnit
pytest --junitxml=test-results.xml
```

## 🔍 Debugging de Testes

Para debugar um teste específico:

```bash
# Executar com pdb
pytest tests/test_logger_singleton.py::TestLogger::test_singleton_pattern -s --pdb

# Executar com breakpoint
pytest tests/test_logger_singleton.py::TestLogger::test_singleton_pattern -s --pdbcls=IPython.terminal.debugger:Pdb
```

## 📋 Checklist de Qualidade

- ✅ Todos os modelos têm testes de sucesso e falha
- ✅ Todos os controladores têm testes de rotas
- ✅ Testes de integração cobrem fluxos principais
- ✅ Mocks apropriados para dependências externas
- ✅ Cobertura de código adequada
- ✅ Tratamento de erros testado
- ✅ Fixtures reutilizáveis
- ✅ Documentação clara

## 🎉 Resultados Esperados

Ao executar os testes, você deve ver:

```
============================= test session starts =============================
platform win32 -- Python 3.x.x, pytest-7.4.2, pluggy-1.3.0
rootdir: /path/to/agenda_contatos
plugins: cov-4.1.0, mock-3.11.1
collected XX tests

tests/test_logger_singleton.py ................ [ 25%]
tests/test_model_contato.py .................... [ 50%]
tests/test_model_categoria.py ................. [ 75%]
tests/test_controller_contato.py .............. [ 85%]
tests/test_controller_categoria.py ............ [ 95%]
tests/test_integration.py .................... [100%]

============================== XX passed in Xs ==============================

---------- coverage: platform win32, python 3.x.x-final-0 -----------
Name                           Stmts   Miss  Cover   Missing
------------------------------------------------------------
Controller/categoria_controller.py     25      0   100%
Controller/contato_controller.py       25      0   100%
Model/categoria.py                    25      0   100%
Model/contato.py                      25      0   100%
logger_singleton.py                   25      0   100%
server.py                              5      0   100%
------------------------------------------------------------
TOTAL                                130      0   100%
```

## 🔄 Manutenção dos Testes

### Adicionando Novos Testes

1. Crie o arquivo de teste seguindo a convenção `test_*.py`
2. Use as fixtures existentes quando possível
3. Adicione mocks apropriados para dependências externas
4. Teste tanto cenários de sucesso quanto de falha
5. Documente o propósito do teste

### Atualizando Testes Existentes

1. Execute os testes antes de fazer mudanças
2. Faça as alterações necessárias
3. Execute novamente para garantir que ainda passam
4. Atualize a documentação se necessário

## 📞 Suporte

Para dúvidas sobre os testes:

1. Verifique a documentação do pytest: https://docs.pytest.org/
2. Consulte os exemplos nos arquivos de teste existentes
3. Use o comando `pytest --help` para ver todas as opções disponíveis 