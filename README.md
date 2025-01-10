progeto de post que faz com python e mysql

para iniciar de pip install -r requirements.txt

depois coloque as cedenciais do mysql no arquivo que estar em
app/database.py

para iniciar de o comando uvicorn app.main:app --reload

tec usadas
fastapi
uvicorn
pydantic
mysql-connector-python
python-multipart
uuid

todas as imagens que der upload vai ficar no uploads e vai ser salva no banco de dados so a o endereço

# 🌉 Sistema de Gerenciamento de post

Sistema desenvolvido para gerenciamento e cadastro de pontes utilizando FastAPI e MySQL.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white)

## 📋 Pré-requisitos

- Python 3.8+
- MySQL Server
- Pip (gerenciador de pacotes Python)

## ⚙️ Configuração do Ambiente

1. Clone o repositório:

```bash
git clone https://github.com/silvakwan1/back_python
cd back_python
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure o banco de dados:

- Abra o arquivo `app/database.py`
- Atualize as credenciais do MySQL:

```python
MYSQL_HOST = "seu_host"
MYSQL_USER = "seu_usuario"
MYSQL_PASSWORD = "sua_senha"
MYSQL_DATABASE = "nome_do_banco"
```

## 🚀 Iniciando o Servidor

Para iniciar o servidor de desenvolvimento:

```bash
uvicorn app.main:app --reload
```

O servidor estará disponível em `http://localhost:8000`

## 📦 Dependências Principais

- FastAPI - Framework web moderno e rápido
- Uvicorn - Servidor ASGI de alta performance
- Pydantic - Validação de dados
- MySQL Connector Python - Driver MySQL
- Python Multipart - Processamento de upload de arquivos
- UUID - Geração de identificadores únicos

## 📁 Estrutura do Projeto

```
sistema-pontes/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   └── ...
│   └── routes/
│       └── ...
│
├── uploads/
├── requirements.txt
└── README.md
```

## 📸 Gerenciamento de Imagens

- Todas as imagens enviadas são armazenadas no diretório `uploads/`
- Apenas o caminho da imagem é salvo no banco de dados
- Sistema gera nomes únicos para cada arquivo usando UUID

## 🔍 Endpoints da API

A documentação completa da API está disponível em:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## ⚠️ Observações Importantes

- Certifique-se de que o MySQL Server está rodando antes de iniciar a aplicação
- Verifique as permissões de escrita no diretório `uploads/`
- Mantenha as credenciais do banco de dados seguras

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.

---
