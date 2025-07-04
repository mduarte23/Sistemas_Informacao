# EngSoftwareII

Projeto desenvolvido para a disciplina de Engenharia de Software II, com o objetivo de aplicar os conceitos de desenvolvimento web. Este projeto integra tecnologias de *Frontend* e *Backend*, proporcionando uma aplicação prática de uma agenda de contatos.

## Status dos Workflows

![Testes](https://github.com/mduarte23/EngSoftwareII/actions/workflows/test.yml/badge.svg)
![Segurança](https://github.com/mduarte23/EngSoftwareII/actions/workflows/security.yml/badge.svg)
![Deploy](https://github.com/mduarte23/EngSoftwareII/actions/workflows/deploy.yml/badge.svg)
![Cobertura](https://codecov.io/gh/mduarte23/EngSoftwareII/branch/main/graph/badge.svg)

## Estrutura do Projeto

O repositório está organizado da seguinte forma:

- **README.md**  
  Este arquivo (o próprio documento) contém a documentação do projeto, instruções de execução, e informações sobre os colaboradores.

- **agenda_contatos/**  
  Diretório principal que agrega os arquivos fonte da aplicação. Abaixo, a descrição detalhada de cada arquivo contido nesta pasta:

  - **index.html**  
    Página inicial da aplicação que define a estrutura visual e a interface do usuário. Aqui são dispostos os elementos de layout, como cabeçalho, formulários para entrada de dados e área para exibição dos contatos. Este arquivo é o ponto de entrada para os navegadores.

  - **styles.css**  
    Arquivo de folha de estilos em CSS3 responsável pela formatação e aparência dos elementos definidos no HTML. Nele são definidas as regras de layout, cores, fontes e comportamentos responsivos para garantir uma boa experiência em diferentes dispositivos.

  - **server.py**  
    Script Python que funciona como o servidor backend da aplicação. Responsável pelo processamento das requisições vindas do frontend, esse arquivo pode incluir:
    - Inicialização de um servidor HTTP simples ou a utilização de frameworks (como Flask ou FastAPI) para gerenciar rotas e endpoints.
    - Processamento e armazenamento dos dados da agenda de contatos.
    - Tratamento de requisições CRUD (Criar, Ler, Atualizar, Excluir) provenientes da interface.

  - **tests/**  
    Diretório contendo todos os testes automatizados do projeto:
    - **test_controller_contato.py**: Testes unitários para o controlador de contatos
    - **test_controller_categoria.py**: Testes unitários para o controlador de categorias
    - **test_integration.py**: 15 testes de integração abrangentes
    - **test_logger_singleton.py**: Testes para o sistema de logging
    - **conftest.py**: Configurações e fixtures do pytest

  - **.github/workflows/**  
    Configurações de automação do GitHub Actions:
    - **test.yml**: Execução automática de testes em múltiplas versões do Python
    - **security.yml**: Verificações de segurança e qualidade de código
    - **deploy.yml**: Deploy automático após testes bem-sucedidos

## Tecnologias Utilizadas

- **Frontend:**
  - **HTML5:** Define a estrutura e os elementos da página.
  - **CSS3:** Responsável pela estilização e layout responsivo.
  - **JavaScript:** Adiciona interatividade e realiza a comunicação com o backend.

- **Backend:**
  - **Python:** Utilizado para criar o servidor e gerenciar a lógica do lado do servidor, possibilitando o processamento e armazenamento dos dados da aplicação.
  - **Flask:** Framework web para criação da API REST
  - **PyMySQL:** Conector para banco de dados MySQL

- **Testes e Qualidade:**
  - **pytest:** Framework de testes
  - **pytest-cov:** Geração de relatórios de cobertura
  - **bandit:** Análise estática de segurança
  - **safety:** Verificação de vulnerabilidades
  - **flake8:** Verificação de estilo de código
  - **black:** Formatação automática de código
  - **isort:** Organização de imports

## Como Executar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/mduarte23/EngSoftwareII.git
   ```

2. **Navegue até a pasta do projeto:**

   ```bash
   cd EngSoftwareII/agenda_contatos
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o backend:**

   ```bash
   python server.py
   ```

5. **Abra a aplicação:**

   Abra o arquivo `index.html` no seu navegador de preferência ou acesse `http://localhost:5000`.

## Executando os Testes

### Testes Locais
```bash
# Executar todos os testes
python -m pytest tests/ -v

# Executar apenas testes de integração
python -m pytest tests/test_integration.py -v

# Executar com cobertura
python -m pytest tests/ --cov=Controller --cov=Model --cov-report=html

# Executar verificações de qualidade
python test_workflows_local.py
```

### Testes Automatizados
Os testes são executados automaticamente no GitHub Actions a cada push ou pull request, incluindo:
- ✅ 41 testes unitários e de integração
- ✅ Verificações de segurança
- ✅ Análise de qualidade de código
- ✅ Geração de relatórios de cobertura

## Funcionalidades

A aplicação foi desenvolvida para gerenciar uma agenda de contatos. Entre as funcionalidades esperadas, destacam-se:

- **Visualização de Contatos:** Exibição dinâmica da lista de contatos cadastrados.
- **Cadastro de Novos Contatos:** Formulário para inserção de dados, com validação para garantir a integridade das informações.
- **Edição e Exclusão:** Opções para atualizar ou remover contatos existentes, com feedback visual para o usuário.
- **Interação Assíncrona:** A utilização de chamadas assíncronas permite que as operações sejam realizadas sem recarregar a página.
- **Gerenciamento de Categorias:** Organização de contatos por categorias.
- **Sistema de Logging:** Registro de todas as operações para auditoria.

## Qualidade e Segurança

O projeto implementa práticas robustas de qualidade de código:

- **15 Testes de Integração** cobrindo cenários completos de uso
- **Cobertura de Código** monitorada via Codecov
- **Análise Estática** de segurança com Bandit
- **Verificação de Vulnerabilidades** com Safety
- **Padronização de Código** com Black e Flake8
- **Organização de Imports** com isort

## Links Úteis

- **Workflows do GitHub Actions:** [https://github.com/mduarte23/EngSoftwareII/actions](https://github.com/mduarte23/EngSoftwareII/actions)
- **Relatório de Cobertura:** [https://codecov.io/gh/mduarte23/EngSoftwareII](https://codecov.io/gh/mduarte23/EngSoftwareII)
- **Documentação dos Testes:** [README_TESTES_INTEGRACAO.md](agenda_contatos/README_TESTES_INTEGRACAO.md)

## Colaboradores

- [Marcelo Duarte](https://github.com/mduarte23)
- [Matheus](https://github.com/matheusmg08)
- [Giovani](https://github.com/gioalves)
