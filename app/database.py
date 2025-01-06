import mysql.connector

# Conexão com o banco de dados
conn = mysql.connector.connect(
    host="localhost",  # Endereço do servidor MySQL
    user="root",  # Usuário do MySQL
    password="",  # Senha do MySQL
    database="meu_banco"  # Nome do banco de dados
)

cursor = conn.cursor()  # Criar um cursor para executar comandos SQL

