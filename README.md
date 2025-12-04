# Projeto Fullstack

Este projeto é uma aplicação fullstack dividida entre frontend e backend.

## Principais tecnologias utilizados

**Back-end:** Python, Flask, SqlAlchemy, Dynaconf, PostgreSQL, Pytest, Httpx, Pydantic, Redis, Angular
**Front-end:** Angular, Bootstrap

## Estrutura principal do Projeto

```
backend
├── app
|    ├── application                   # Lógica do negócio
|    ├── domain                        # Regras de negócio
|    ├── infra                         # Dependências externas
|    ├── presentation                  # Exposição da aplicação
|    ├── create_app.py                 # Criação do app
|    ├── create_produto_worker.py      # Criação do worker de produtos
|    ├── create_usuario_worker.py      # Criação do worker de usuário
├── tests
|   ├── functional         # Testes funcionais da integração
│   └── conftest.py        # Fixtures dos testes
├── .env                   # Arquivo que informa o ambiente para o dynaconf(somente para uso local)
├── Dockerfile-app         # Instruções para construir a imagem Docker do backend
├── Dockerfile-pqsql       # Instruções para construir a imagem Docker do banco de dados
├── Dockerfile-redis       # Instruções para construir a imagem Docker do banco Redis
├── main.py                # Ponto de entrada da aplicação
├── produto_worker.py      # Ponto de entrada do worker de produto
├── pyproject.toml         # Lista de dependências do projeto
|── settings.toml          # Configurações usadas pelo Dynaconf baseado no ambiente em que a aplicação está rodando
├── supervisord.conf       # Arquivo de configuração do controle de processos que executa o app e os workers
├── usuario_worker.py      # Ponto de entrada do worker de usuario
frontend
├── src
|   ├── app
|        ├── components    # Componentes da página do projeto
|        ├── interfaces    # Classe com interfaces usadas para declaração de objetos
|        ├── route_guard   # Funções para controle de rotas e validade de token
|        ├── services      # Serviços http para consumo das rotas do backend
| Dockerfile-angular       # Instruções para construir a imagem Docker do frontend
docker-compose-projeto-fullstack    # Compose de todos os containers
.gitignore                          # Pastas/arquivos para não enviar para o repo

```

## Pré-requisitos

- Python 3.13+ ou superior
- Node 24+
- Docker

## Instalação

Clone o projeto

```bash
git clone https://github.com/everthefullstack/projeto_fullstack
```

## Executando a Aplicação

Para construir e executar a aplicação usando Docker, siga os passos abaixo:

Escolha qual ambiente você quer usar. Baseado no ambiente, algumas configurações são diferentes.\
As configurações em default, serão válidas para todos os ambientes.\
Dentro do arquivo settings.toml existem as configurações que serão usadas para cada ambiente.\
Por exemplo, se usar o development, o banco de dados é X, se for production é Y.\
Para isso, altere o valor da variável dentro do arquivo Dockerfile-app, como por exemplo:
Se for testar localmente, faça essa alteração no arquivo .env, caso rode com o flask com o app.run()

```bash
ENV ENV_FOR_DYNACONF=production
```

Ou

```bash
ENV ENV_FOR_DYNACONF=development
```

Construa as imagem Docker com docker compose:

```bash
docker-compose -f docker-compose-projeto-fullstack.yml up --build -d
```

Para deletar tudo:

```bash
docker-compose down -v
```

A aplicação backend estará disponível em `http://localhost:8000`.\
A aplicação frontend estará disponível em `http://localhost:4200`.

Para executar os teste:

```bash
pytest tests -v --cov=app
```

## Possíveis melhorias

Para uma aplicação tão pequena, poderia também ter sido feita com MVC.\
Para uma melhor performance, seria interessante refatorar o código para uma metodologia async.\
A utilização de logs para observabilidade também seria interessante, a modo de gerar métricas e/ou tomada de ações.