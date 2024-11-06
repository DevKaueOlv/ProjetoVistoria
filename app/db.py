import pyorient
import os
from dotenv import load_dotenv

# Carregando as variáveis de ambiente
load_dotenv()

def get_db_connection():
    host = os.getenv("ORIENTDB_HOST")  # Geralmente 'localhost'
    port = os.getenv("ORIENTDB_PORT")  # Porta 2480 para conexões via HTTP
    user = os.getenv("ORIENTDB_USER")  # Usuário do banco de dados
    password = os.getenv("ORIENTDB_PASSWORD")  # Senha do banco
    db_name = os.getenv("ORIENTDB_DB")  # Nome do banco de dados, no seu caso 'ProjetoVistoria'

    # Verificar se todas as variáveis estão configuradas corretamente
    if not host or not port or not user or not password or not db_name:
        raise ValueError("Alguma variável de ambiente está faltando!")

    print(f"Conectando ao OrientDB em {host}:{port}...")

    try:
        # Tenta conectar ao servidor OrientDB através de HTTP
        client = pyorient.OrientDB(host, int(port))  # Usando a classe OrientDB para HTTP
        client.connect(user, password)  # Autentica com o usuário e senha
        client.db_open(db_name, user, password)  # Conecta ao banco de dados especificado
        print(f"Conexão estabelecida com o banco de dados {db_name}.")
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        raise

    return client
